import os
import time
import json
import paramiko
from nr_interactions import update_terminal_server_access
from dotenv import load_dotenv
import datetime
load_dotenv()

ssh_username = os.getenv("SSH_USERNAME")
ssh_password = os.getenv("SSH_PASSWORD")

try:
    file = open("dc_list.json")
    data = json.load(file)

    ts = data["ts"]

    nr_data = []

    for item in ts:
        server = item["name"]
        print("Checking terminal server access for: " + server)
        for line in item["lines"]:
            port = 5000 + line["ROTY"]
            tty = line["TTY"]
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("\nConecting to device on port " + str(port) + "\n")
            connected = False
            try:
                ssh_client.connect(
                    hostname=server, port=port, username=ssh_username, password=ssh_password, timeout=10)
                connected = True
            except Exception as e:
                print("Unable to connect: " + str(e))
                print("\n###########################")

            if not connected:
                continue

            # Invoke interactive shell on the jump device
            conn = ssh_client.invoke_shell()
            conn.send("\n")

            # Wait while the response is not ready or the buffer timeout
            buffer_timeout = 20
            while not conn.recv_ready() and buffer_timeout:
                print("NOT READY - recv_ready: " +
                      str(conn.recv_ready()) + "\n")
                time.sleep(1)
                buffer_timeout -= 1

            # If timeout, means unable to connect to this terminal console server on the corresponding line
            if not buffer_timeout:
                print("Unable to access device on port " + str(port))
            else:
                output = conn.recv(2000).decode('utf-8')
                print(output)
                if "user" in output.lower():
                    conn.send(ssh_username + "\n")
                    buffer = 5
                    while not conn.recv_ready() and buffer:
                        print("NOT READY - recv_ready: " +
                              str(conn.recv_ready()) + "\n")
                        time.sleep(1)
                        buffer -= 1
                    response = conn.recv(2000).decode('utf-8')
                    print(response)
                    if "password" in response.lower():
                        conn.send(ssh_password + "\n")
                        buffer = 5
                        while not conn.recv_ready() and buffer:
                            print("NOT READY - recv_ready: " +
                                  str(conn.recv_ready()) + "\n")
                            time.sleep(1)
                            buffer -= 1
                        response = conn.recv(2000).decode('utf-8')
                        print(response)
                        response = response.splitlines()
                        for val in response:
                            if len(val):
                                device = val[:-1]
                                break
                        print("Device connected to port " +
                              str(port) + " is: " + device)
                        nr_data.append({
                            "server": server,
                            "line": tty,
                            "port": port,
                            "device": device,
                            "last_tested": str(datetime.datetime.now())
                        })
                    else:
                        print("Unhandled Response")
                elif "login" in output.lower():
                    response = output.splitlines()
                    for val in response:
                        if len(val):
                            val = val.split()
                            device = val[0]
                            break
                    print("Device connected to port " +
                          str(port) + " is: " + device)
                    nr_data.append({
                        "server": server,
                        "line": tty,
                        "port": port,
                        "device": device,
                        "last_tested": str(datetime.datetime.now())
                    })
                elif "#" in output.lower():
                    response = output.splitlines()
                    for val in response:
                        if len(val):
                            device = val[:-1]
                            break
                    print("Device connected to port " +
                          str(port) + " is: " + device)
                    nr_data.append({
                        "server": server,
                        "line": tty,
                        "port": port,
                        "device": device,
                        "last_tested": str(datetime.datetime.now())
                    })
                else:
                    print("Unhandled Response")
            print("\n###########################")

    print("Data: " + str(nr_data))
    # # Update new relic metric information
    # update_terminal_server_access()
    # print("New relic Metric information updated")

except Exception as e:
    print("Something went wrong: " + str(e))

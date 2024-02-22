import os
import time
import json
import paramiko
from nr_interactions import update_terminal_server_access
from dotenv import load_dotenv
import datetime
load_dotenv()

usernames = [os.getenv("TACACS_USERNAME"), os.getenv(
    "NETADMIN_SU_USERNAME"), os.getenv("NETADMIN_USERNAME")]
passwords = [os.getenv("TACACS_PASSWORD"), os.getenv(
    "NETADMIN_SU_PASSWORD"), os.getenv("NETADMIN_PASSWORD")]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def ssh_connect(server, port, idx):
    ssh_username = usernames[idx]
    ssh_password = passwords[idx]
    try:
        ssh_client.connect(
            hostname=server, port=port, username=ssh_username, password=ssh_password, timeout=10)
    except Exception as e:
        print("Unable to connect to " + server + " on " + port)


def valid_hostname(device):
    device = device.replace('-', '')
    return not device.isdigit()


def check_login(conn, idx):
    conn.send(usernames[idx] + "\n")
    buffer = 5
    while not conn.recv_ready() and buffer:
        print("NOT READY - recv_ready: " +
              str(conn.recv_ready()) + "\n")
        time.sleep(1)
        buffer -= 1
    response = conn.recv(20000).decode('utf-8')
    print(response)
    if "password" in response.lower():
        conn.send(passwords[idx] + "\n")
        buffer = 5
        while not conn.recv_ready() and buffer:
            print("NOT READY - recv_ready: " +
                  str(conn.recv_ready()) + "\n")
            time.sleep(1)
            buffer -= 1
        response = conn.recv(20000).decode('utf-8')
        print(response)
        response = output.splitlines()
        for val in response:
            print("VAL: " + val)


try:
    file = open(
        "/home/singhnavneet.su/console-access-automation/dc_list.json")
    data = json.load(file)

    ts = data["ts"]

    nr_data = []

    for item in ts:
        server = item["name"]
        print("Checking terminal server access for: " + server)
        for line in item["lines"]:
            port = 5000 + line["ROTY"]
            tty = line["TTY"]

            print("\nConecting to device on port " + str(port) + "\n")

            ssh_username = usernames[0]
            ssh_password = passwords[0]

            connected = False
            try:
                ssh_connect(server, port, 0)
                connected = True
            except Exception as e:
                print("Unable to connect to " + server + " on " + str(port))
                print("\n###########################")
                nr_data.append({
                    "server": server,
                    "line": tty,
                    "port": port,
                    "device": "",
                    "last_tested": str(datetime.datetime.now()),
                    "device_available": "false"
                })

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
                print("\n###########################")
                nr_data.append({
                    "server": server,
                    "line": tty,
                    "port": port,
                    "device": "",
                    "last_tested": str(datetime.datetime.now()),
                    "device_available": "false"
                })
            else:
                decode = True
                try:
                    output = conn.recv(20000).decode('utf-8')
                    print(output)
                except Exception as e:
                    print("Unable to decode the output: " + str(e))
                    decode = False
                    nr_data.append({
                        "server": server,
                        "line": tty,
                        "port": port,
                        "device": "",
                        "last_tested": str(datetime.datetime.now()),
                        "device_available": "false"
                    })
                if decode:
                    if "user" in output.lower():
                        conn.send(ssh_username + "\n")
                        buffer = 5
                        while not conn.recv_ready() and buffer:
                            print("NOT READY - recv_ready: " +
                                  str(conn.recv_ready()) + "\n")
                            time.sleep(1)
                            buffer -= 1
                        response = conn.recv(20000).decode('utf-8')
                        print(response)
                        if "password" in response.lower():
                            conn.send(ssh_password + "\n")
                            buffer = 5
                            while not conn.recv_ready() and buffer:
                                print("NOT READY - recv_ready: " +
                                      str(conn.recv_ready()) + "\n")
                                time.sleep(1)
                                buffer -= 1
                            response = conn.recv(20000).decode('utf-8')
                            print(response)
                            response = response.splitlines()
                            for val in response:
                                if len(val):
                                    device = val[:-1]
                                    break
                            print("Device connected to port " +
                                  str(port) + " is: " + device)
                            if not valid_hostname(device):
                                print("Test different credentials")
                                check_login(conn, 1)
                            nr_data.append({
                                "server": server,
                                "line": tty,
                                "port": port,
                                "device": device,
                                "last_tested": str(datetime.datetime.now()),
                                "device_available": "true"
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
                        if not valid_hostname(device):
                            print("Test different credentials")
                            check_login(conn, 1)
                        nr_data.append({
                            "server": server,
                            "line": tty,
                            "port": port,
                            "device": device,
                            "last_tested": str(datetime.datetime.now()),
                            "device_available": "true"
                        })
                    elif "#" in output.lower():
                        response = output.splitlines()
                        for val in response:
                            if len(val):
                                device = val[:-1]
                                break
                        print("Device connected to port " +
                              str(port) + " is: " + device)
                        if not valid_hostname(device):
                            print("Test different credentials")
                            check_login(conn, 1)
                        nr_data.append({
                            "server": server,
                            "line": tty,
                            "port": port,
                            "device": device,
                            "last_tested": str(datetime.datetime.now()),
                            "device_available": "true"
                        })
                    elif "password" in output.lower():
                        conn.send(ssh_password + "\n")
                        buffer = 5
                        while not conn.recv_ready() and buffer:
                            print("NOT READY - recv_ready: " +
                                  str(conn.recv_ready()) + "\n")
                            time.sleep(1)
                            buffer -= 1
                        response = conn.recv(20000).decode('utf-8')
                        print(response)
                        response = response.splitlines()
                        for val in response:
                            if len(val):
                                device = val[:-1]
                                break
                        print("Device connected to port " +
                              str(port) + " is: " + device)
                        if not valid_hostname(device):
                            print("Test different credentials")
                            check_login(conn, 1)
                        nr_data.append({
                            "server": server,
                            "line": tty,
                            "port": port,
                            "device": device,
                            "last_tested": str(datetime.datetime.now()),
                            "device_available": "true"
                        })
                    else:
                        print("Unhandled Response")
                print("\n###########################")

    print("Data: " + str(nr_data))
    # Update new relic metric information
    # update_terminal_server_access(nr_data)
    # print("New relic Metric information updated")

except Exception as e:
    print("Something went wrong: " + str(e))

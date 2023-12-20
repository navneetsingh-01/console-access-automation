import os
import time
import json
import paramiko
from nr_interactions import update_terminal_server_access
from dotenv import load_dotenv
load_dotenv()

ssh_username = os.getenv("SSH_USERNAME")
ssh_password = os.getenv("SSH_PASSWORD")


def get_device(line):
    line = line.split()
    return line[0]


try:
    file = open("dc_list.json")
    data = json.load(file)

    ts = data["ts"]

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
                if "username" in output.lower():
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
                else:
                    print("Get device name")
                # output = output.split("\n")
                # for line in output:
                #     # Handles -> Username:
                #     if "username:" in line.lower():
                #         # Assume the device to be connected will be same as the expected device in the inventory
                #         print("Device connected to port " +
                #               str(server["port"]) + " is: " + expected_device)
                #     # Handles -> <device> login:
                #     if "login:" in line.lower():
                #         connected_device = get_device(line)
                #         if expected_device.lower() in connected_device.lower():
                #             print("Device connected to port " +
                #                   str(server["port"]) + " is: " + expected_device)
                #         else:
                #             print("Expected device connected for port " +
                #                   str(server["port"]) + " is: " + expected_device)
                #             print("Device found: " + connected_device)

            print("\n###########################")

    # # Update new relic metric information
    # update_terminal_server_access()
    # print("New relic Metric information updated")

except Exception as e:
    print("Something went wrong: " + str(e))

import json
import os
import paramiko

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
        print(str(e))
        print("Unable to connect to " + server + " on " + port)


try:
    servers = []

    # file = open(
    #     "/home/singhnavneet.su/console-access-automation/dc_list_complete.json")
    file = open(
        "/Users/singhnavneet/Documents/projects/console_access /dc_list_complete.json")
    data = json.load(file)
    ts = data['ts']
    for item in ts:
        server = item['name']
        servers.append(server)
except Exception as e:

    print("Something went wrong: " + str(e))

print(servers)
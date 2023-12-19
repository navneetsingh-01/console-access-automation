import os
import json
import paramiko
from dotenv import load_dotenv
load_dotenv()

ssh_username = os.getenv("SSH_USERNAME")
ssh_password = os.getenv("SSH_PASSWORD")

try:
    file = open("dc_list.json")
    data = json.load(file)
    ts = data["ts"]
    for item in ts:
        server = item["name"]
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connected = False
        try:
            client.connect(hostname=server, port=22,
                           username=ssh_username, password=ssh_password, timeout=10)
            connected = True
        except Exception as e:
            print("Unable to connect to " + server + ": " + str(e))
            continue
        print("Connected to " + server)
        stdin, stdout, stderr = client.exec_command('sh line')
        print("output: ", stdout)
        print("error: ", stderr)
except Exception as e:
    print(str(e))

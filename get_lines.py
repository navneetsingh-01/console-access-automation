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
        output = stdout.read().decode()
        error = stderr.read().decode()
        print("output: ", output)
        if error:
            print("error: ", error)
        i = 0
        output = output.split()
        while i < len(output) and "tty" not in output[i].lower():
            i += 1
        output = output[i:]
        print(output)
        # for idx, val in enumerate(output):
        #     if idx%6==0:
        #         print(val)

except Exception as e:
    print(str(e))

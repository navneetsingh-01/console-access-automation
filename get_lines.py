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
    for ts_idx, item in enumerate(ts):
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
        response = {}
        roty = 1
        for line in (output.splitlines()):
            if 'TTY' in line:
                cur = line.split()
                idx=0
                if cur[idx] == "*":
                    idx+=1
                req = cur[idx]
                req = req.replace("*", '')
                response[roty]=req
                roty+=1
        for rty, tty in response.items():
            data[ts_idx]["lines"].append({"ROTY": rty, "TTY": tty})

    json_object = json.dumps(data, indent=4)
    with open("dc_list.json", "w") as outfile:
        outfile.write(json_object)
       
except Exception as e:
    print(str(e))

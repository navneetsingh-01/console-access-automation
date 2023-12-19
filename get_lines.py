import os
import json
from dotenv import load_dotenv
load_dotenv()

ssh_username = os.getenv("SSH_USERNAME")
ssh_password = os.getenv("SSH_PASSWORD")

try:
    file = open("dc_list.json")
    data = json.load(file)
    for item in data:
        server = item["name"]
        print(server)
except Exception as e:
    print(str(e))

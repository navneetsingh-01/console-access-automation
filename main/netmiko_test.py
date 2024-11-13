import os
import paramiko
from netmiko  import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="syd4-ts",
    username=os.getenv("TACACS_USERNAME"),
    password=os.getenv("TACACS_PASSWORD"),
)

try: 
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(net_connect.find_prompt())
    net_connect.disconnect()
except Exception as e:
    print("Something went wrong: " + str(e))
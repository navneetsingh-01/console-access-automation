import os
import paramiko
from netmiko import ConnectHandler
from getpass import getpass


try:
    net_connect = ConnectHandler(
        device_type="cisco_ios",
        host="fra4-ts",
        username=os.getenv("TACACS_USERNAME"),
        password=getpass(),
    )
    output = net_connect.send_command("show ip interface brief")
    print(output)
    print(net_connect.find_prompt())
    net_connect.disconnect()
except Exception as e:
    print("Something went wrong: " + str(e))

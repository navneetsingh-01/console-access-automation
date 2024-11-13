import os
from netmiko  import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_ios_telnet",
    host="syd4-ts",
    username=os.getenv("TACACS_USERNAME"),
    password=os.getenv("TACACS_PASSWORD"),
)

print(net_connect.find_prompt())
net_connect.disconnect()

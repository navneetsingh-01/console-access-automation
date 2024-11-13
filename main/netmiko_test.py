import os
from netmiko  import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="syd4-ts",
    username=os.getenv("TACACS_USERNAME"),
    password=os.getenv("TACACS_PASSWORD"),
    port=5005
)

try: 
    print(net_connect.find_prompt())
    net_connect.disconnect()
except Exception as e:
    print("Something went wrong: " + str(e))
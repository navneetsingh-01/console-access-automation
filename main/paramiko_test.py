import paramiko
import time
import os

# Create SSH client
try:

    client = paramiko.SSHClient()

    # Set policy to automatically add hosts to known hosts file
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote host
    client.connect(
        hostname="fra4-ts",
        username=os.getenv("TACACS_USERNAME"),
        password=os.getenv("TACACS_PASSWORD"),
        port=22
    )

    # # Open an interactive SSH session
    # ssh_client = client.invoke_shell()

    # # Send command
    # ssh_client.send("sh ip int bri\n")

    # # Wait for the command to be finished
    # time.sleep(3)

    # # Receive and process command output
    # output = ssh_client.recv(65000)
    # print(output.decode("ascii"))

    # # Close the SSH session
    # ssh_client.close()

    # # Close the connection
    # client.close()

except paramiko.AuthenticationException:
    print("Authentication failed. Please verify your credentials.")

except Exception as e:
    print("Something went wrong: " + str(e))
import paramiko
import time

# Create SSH client
client = paramiko.SSHClient()

# Set policy to automatically add hosts to known hosts file
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote host
client.connect(
    hostname="fra4-ts",
    username="singhnavneet.su",
    password="mC$<4?7H{nocR\Emilj=",
)

# Open an interactive SSH session
ssh_client = client.invoke_shell()

# Send command
ssh_client.send("sh ip int bri\n")

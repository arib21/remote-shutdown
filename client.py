import socket

hostname = "0.0.0.0"
port = 28974

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((hostname, port))
    print("Shutting down remote machine...")

except socket.error as error:
    print(f"Couldn't connect to Host::{hostname} Port::{port}")
    print(error)

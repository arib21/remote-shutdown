import socket
import os

hostname = socket.gethostname() # Make sure the output of this matches with the client.py script
port = 28974 # Make sure the port matches with the port in the client.py script

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostname, port))

server.listen(1)
print(f"Server listening on Port::{port} Host::{hostname}")

while True:
    client, client_address = server.accept()
    print(f"Connection from address {client_address}")
    os.system("shutdown /s /t 1") # You can change the string here with whatever command you like!

import socket
import os

hostname = socket.gethostname()
port = 28974

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostname, port))

server.listen(1)

while True:
    client, client_address = server.accept()
    os.system("shutdown /s /t 1")
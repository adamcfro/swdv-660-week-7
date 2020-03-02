import socket
from caesar_cipher import encrypt

# LISTEN FOR SERVER
server_to_CA = socket.socket()
host = '127.0.0.1'
port = 9501
server_to_CA.bind((host, port))
server_to_CA.listen(5)

# LISTEN FOR CLIENT
client_to_CA = socket.socket()
host = '127.0.0.1'
port = 9502
client_to_CA.bind((host, port))
client_to_CA.listen(5)

s, addr = server_to_CA.accept()
c, addr = client_to_CA.accept()

servername = []
keyname = []

# STORE SERVER INFORMATION
data = s.recv(1024).decode()
if data == "servername":
    print(f"CA received this information from server: {data}")
    servername.append(data)
    keyname.append('key')
s.close()

# SEND CLIENT INFORMATION
new_data = c.recv(1024).decode()
if new_data in servername:
    print(f"CA received this request from client: {data}")
    c.send(keyname[0].encode())
c.close()

import socket
from caesar_cipher import encrypt

host = '127.0.0.1'
port = 9500

ca = '127.0.0.1'
ca_port = 9501

servername = 'servername'
key = 'key'

# CREATE CONNECTION FOR CA
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ca, ca_port))
s.send(servername.encode())
s.close()

# CREATE SOCKET FOR CLIENT
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((host, port))
ss.listen()
c, addr = ss.accept()

while True:
    data = c.recv(1024).decode()
    # PROVIDE CLIENT WITH SERVER NAME
    if data == "request server name":
        print(f"Server received this request from client: {data}")
        c.send(servername.encode())
    # VALIDATE AND SEND CLIENT ACKNOWLEDGMENT
    elif data == encrypt('sessioncipherkey', key):
        print(f"Server received proper key from client")
        acknowledgment = encrypt("sessioncipherkeyacknowledgment", key)
        c.send(acknowledgment.encode())
        print("Ready for transmission...")
    elif data == encrypt("Final transmission", key):
        print("Final message received")
    # CLOSE SERVER
    else:
        print(f"Server done receiving")
        s.close()
        break

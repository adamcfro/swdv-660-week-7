import socket
from caesar_cipher import encrypt

host = '127.0.0.1'
port = 9500
ca_port = 9502

# REQUEST INFORMATION FROM SERVER
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', port))
    s.send("request server name".encode())
    data = s.recv(1024).decode()
    print(f"Client received this information from server: {data}")

    # REQUEST INFORMATION FROM CA
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as t:
        t.connect((host, ca_port))
        t.send(data.encode())
        key = t.recv(1024).decode()
        print(f"Client received this from CA: {key}")

        t.close()

    # VERIFY KEY WITH SERVER
    encrypted_message = encrypt('sessioncipherkey', key)
    s.send(encrypted_message.encode())
    print("Client sent encrypted message to server")
    # RECEIVE ENCRYPTED MESSAGE AND VERIFY MESSAGE
    data = s.recv(1024).decode()
    if data == encrypt("sessioncipherkeyacknowledgment", key):
        # ENCRYPT MESSAGE USING KEY
        message = encrypt('Final transmission', key)
        s.send(message.encode())
        print("Sending final message")

    s.close()

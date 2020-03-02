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
        new_data = t.recv(1024).decode()
        print(f"Client received this from CA: {new_data}")

        t.close()

    # VERIFY KEY WITH SERVER
    encrypted_message = encrypt('sessioncipherkey', new_data)
    s.send(encrypted_message.encode())
    # RECEIVE ENCRYPTED MESSAGE
    more_new_data = s.recv(1024).decode()
    if more_new_data == encrypt("sessioncipherkeyacknowledgment", new_data):
        # ENCRYPT MESSAGE USING KEY
        s.send("Final transmission".encode())

    s.close()

import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)  
server_socket.bind(server_address)


server_socket.listen(1)

print("Waiting for a connection...")
connection, client_address = server_socket.accept()
print("Connected to:", client_address)

try:
    while True:
        data = connection.recv(1024).decode()
        if data:
            print(f"Received: {data}")
            connection.sendall("Message received!".encode())
except KeyboardInterrupt:
    pass
finally:
    connection.close()
    server_socket.close()

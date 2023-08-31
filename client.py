import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)  
client_socket.connect(server_address)

try:
    message = "Hello, server!"
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024).decode()
    print(f"Received from server: {data}")
finally:
    client_socket.close()

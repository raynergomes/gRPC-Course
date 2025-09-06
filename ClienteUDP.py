import socket

# Client side
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

message = "Hello Word!"
client_socket.sendto(message.encode(), server_address)
print(f"Sent message to server: {message}")

data, address = client_socket.recvfrom(1024)
print(f"Received message from server: {data.decode()}")

client_socket.close()
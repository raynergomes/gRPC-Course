import socket

# Server side
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("UDP server listening on port 12345")

while True:
    data, address = server_socket.recvfrom(1024)
    print(f"Received message from {address}: {data.decode()}")

    message = "Hello Word!"
    server_socket.sendto(message.encode(), address)
    print(f"Sent message to {address}: {message}")
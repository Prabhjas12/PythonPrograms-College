import socket
import threading
host = '127.0.0.1'  
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                remove(client)
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                remove(client_socket)
                break
            else:
                broadcast(message, client_socket)
        except:
            continue
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                remove(client_socket)
                break
            elif message == "/quit":
                remove(client_socket)
                client_socket.send("You are now disconnected.".encode('utf-8'))
                break
            else:
                broadcast(message, client_socket)
        except:
            continue
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    print(f"Client {client_address} connected.")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()


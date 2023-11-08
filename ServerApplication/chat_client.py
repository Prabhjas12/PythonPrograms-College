import socket
import threading
host = '127.0.0.1' 
port = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
def send_message():
    while True:
        message = input()
        client.send(message.encode('utf-8'))
        if message == "/quit":
            client.close()
            break
def receive_message():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred. Disconnecting...")
            client.close()
            break
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()

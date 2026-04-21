import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()
print("Waiting for Mazin to connect...")

# Guardamos la conexión directa
connection, address = server.accept()
print("✅ Mazin has connected!")

def listen_messages():
    while True:
        message = connection.recv(1024).decode('utf-8')
        print(f"\nMazin: {message}")

def send_messages():
    while True:
        my_message = input("Me: ")
        connection.send(my_message.encode('utf-8'))

threading.Thread(target=listen_messages).start()
threading.Thread(target=send_messages).start()
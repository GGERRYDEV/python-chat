import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP de tu ordenador en la red local
client.connect(('10.201.82.94', 5555))
print("✅ Connected to Gerard's server.")

def listen_messages():
    while True:
        message = client.recv(1024).decode('utf-8')
        print(f"\nGerard: {message}")

def send_messages():
    while True:
        my_message = input("Me: ")
        client.send(my_message.encode('utf-8'))

threading.Thread(target=listen_messages).start()
threading.Thread(target=send_messages).start()
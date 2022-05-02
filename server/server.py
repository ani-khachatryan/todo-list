import socket
from send_notifs import SendNotifications
from datetime import datetime
import time as t
from database import RequestHandler
import threading
import requests

HEADER = 64
PORT = 5050
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
SERVER = s.getsockname()[0]
s.close()
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "exit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                print(f"[{addr}] {msg}")
                lis  = RequestHandler(msg)
                send_str = ""
                for i in lis:
                    send_str = send_str +str(i) + " loremipsum "
                conn.send(send_str.encode(FORMAT))       
    conn.close()

def check_and_send():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        start = '23:47:00'
        end = '23:47:04'
        if current_time > start and current_time < end:
            print ("Sending...")
            SendNotifications()
            t.sleep(5)
#        print ("Hello")
#        t.sleep(10)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    thread1 = threading.Thread(target=check_and_send)
    thread1.start()
    while True:
        conn, addr = server.accept()
        thread2 = threading.Thread(target=handle_client, args=(conn, addr))
        thread2.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")

print("[STARTING] server is starting...")
start()

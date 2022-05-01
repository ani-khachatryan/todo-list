import socket
#TODO:import interface

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "exit"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
SERVER = s.getsockname()[0]
s.close()
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    if operation_type == "login":
        clientMessage = str("OP_LOGIN " + username + " " + password)
        send(clientMessage)
    elif operation_type == "registr":
        clientMessage = str("OP_NEWUSER " + name + " " + username + " " + password + " " + email)
        send(clientMessage)
    elif operation_type == "get tasks":
        clientMessage = str("TASK_GET " + user_id + " " + date)
        send(clientMessage)
    elif operation_type == "add task":
        clientMessage = str("TASK_ADD " + user_id + " " + description + " " + date)
        send(clientMessage)
    elif operation_type == "delete task":
        clientMessage = str("TASK_DELETE " + task_id)
        send(clientMessage)
    #else:
    #    send("client Disconnected")
    #    send(DISCONNECT_MESSAGE)
    #    break

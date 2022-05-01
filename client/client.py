import socket


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
    return client.recv(2048).decode(FORMAT)

def login(username, password):
    clientMessage = str("OP_LOGIN " + username + " " + password)
    send(clientMessage)
def registration(name, username, password, email):
    clientMessage = str("OP_NEWUSER " + name + " " + username + " " + password + " " + email)
    send(clientMessage)
def get_tasks(user_id, date):
    clientMessage = str("TASK_GET " + user_id + " " + date)
    send(clientMessage)
def add_task(user_id, description, date):
    clientMessage = str("TASK_ADD " + user_id + " " + description + " " + date)
    send(clientMessage)
def delete_task(task_id):
    clientMessage = str("TASK_DELETE " + task_id)
    send(clientMessage)
    #if:
    #    send("client Disconnected")
    #    send(DISCONNECT_MESSAGE)
    #    break

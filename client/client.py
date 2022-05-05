from datetime import datetime
import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "exit"
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(("8.8.8.8", 80))
#SERVER = s.getsockname()[0]
#s.close()
SERVER = "192.168.1.122"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
#print(SERVER)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(2048).decode(FORMAT).split(" loremipsum ")

def login(username, password):
    clientMessage = f'OP_LOGIN {username} {password}'
    #User.id = 
    result = send(clientMessage)
    if len(result) == 1:
        return result[0]
    else:
        User.id = result[0]
        return True

def registration(name, username, password, email):
    clientMessage = f'OP_NEWUSER {name} {username} {password} {email}'
    result = send(clientMessage)[0]
    if result == "OK":
        return True
    else:
        return False

class User:
    def get_tasks(self, date = datetime.today().strftime('%Y-%m-%d')):
        clientMessage = f"TASK_GET {self.id} {str(date)}"
        return send(clientMessage)

    def add_task(self, description, date):
        clientMessage = f'TASK_ADD {self.id} {description} {str(date)}'
        return send(clientMessage)

    def delete_task(self, task_id):
        clientMessage = f'TASK_DELETE {task_id}'
        send(clientMessage)
        return
    #if:
    #    send("client Disconnected")
    #    send(DISCONNECT_MESSAGE)
    #    break

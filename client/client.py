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
    result = send(clientMessage)
    if result[0].startswith("Error"):
        return False
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
    def get_tasks(date = datetime.today().strftime('%Y-%m-%d')):
        clientMessage = f"TASK_GET {User.id} {str(date)}"
        tasks = send(clientMessage)
        if tasks[0] == "No Tasks":
            return []
        tasks = tasks[:-1]
        for i in range(len(tasks)):
            tasks[i] = tasks[i][1:-1]
            tasks[i] = tasks[i].split(', ')
            tasks[i][0] = int(tasks[i][0])
            tasks[i][1] = int(tasks[i][1])
            tasks[i][2] = tasks[i][2][1:-1]
            tasks[i][3] = tasks[i][3][1:-1]
        return tasks

    def add_task(description, date):
        clientMessage = f'TASK_ADD {User.id} {description} {str(date)}'
        return send(clientMessage)

    def delete_task(task_id):
        clientMessage = f'TASK_DELETE {task_id}'
        send(clientMessage)
    #if:
    #    send("client Disconnected")
    #    send(DISCONNECT_MESSAGE)
    #    break

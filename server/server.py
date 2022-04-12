import sys
import sqlite3


def print_db(cursor):
    for row in cursor.execute('SELECT * FROM users'):
        print(row)

def Connect(path):
    try:
        connection = sqlite3.connect(path)
    except Error:
        print(Error)
    return connection

def RequestHandler(req):
    # assume request is a list
    path = os.path.abspath("todo.db")
    connection = Connect(path)
    cursor = connection.cursor()
    if req[0] == "OP_GETTASKS":
          pass
    elif req[0] == "OP_ADD":
        pass
    elif req[0] == "OP_DELETE":
        delete_task = '''DELETE from tasks WHERE "id" = ?'''
        #tldr
    elif req[0] == "get_todays_tasks":
        get_tasks = '''SELECT * from tasks WHERE "user_id" = ?'''
        tasks = cursor.execute(get_tasks, req[1])
        #exec
        #return tasks to whoever was asking
    elif req[0] == "OP_LOGIN":
        get_query = '''SELECT * from users WHERE "username" = ?'''
        try:
            usr = cursor.execute(get_query, req[1])
            #connection.commit?
            #assume usr is a list
        except Error:
            print("Error: Wrong username.")
        if usr[3] == req[2]:
            #message OK
            pass
        else:
            print("Error: Wrong password."


    elif req[0] == "OP_NEWUSER":
        try:
            insert_query = '''INSERT INTO users
            (name, username, password, telegram)
            VALUES (?, ?, ?, ?)'''
            cursor.execute(insert_query, req[1:])
            connection.commit()
        except Error:   
           print("User with this telegram already exists")
    else:
        print("Error: Unknown request")
        sys.exit()
    print_db(cursor)
    cursor.close()
    if connection:
        connection.close()

def main():
    #while True:
    #    //blabla
    #    RequestHandler(request)
    RequestHandler(["OP_NEWUSER", "Mher", "involid", 661681731])

main()

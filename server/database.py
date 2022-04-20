import os
import sys
import sqlite3


def print_db(cursor):
    for row in cursor.execute('SELECT * FROM users'):
        print(row)

def Connect(path):
    try:
        connection = sqlite3.connect(path)
        return connection
    except sqlite3.Error as err:
        print(err)

def RequestHandler(req):
    # assume request is a list
    path = os.path.abspath("todo.db")
    connection = Connect(path)
    cursor = connection.cursor()
    if req[0] == "TASK_GET":
        '''req[1] user_id, req[2] date'''
        get_tasks = '''SELECT * FROM tasks WHERE "user_id" = ? "date" = ?'''
        ans = list(cursor.execute(get_tasks, req[1:]))
        # return ans to client or bot
    elif req[0] == "TASK_ADD":
        '''(unique task_id is generated) req[1] user_id, req[2] description, req[3] date'''
        add_task = '''INSERT INTO tasks
        (user_id, description, date)
        VALUES (?, ?, ?)'''
        cursor.execute(add_task, req[1:])
        connection.commit()
        # TODO update tasks in clients page
        # display "Added task" message
    elif req[0] == "TASK_DELETE":
        '''req[1] task_id'''
        delete_task = '''DELETE from tasks WHERE "task_id" = ?'''
        cursor.execute(delete_task, req[1])
        connection.commit()
        # TODO update tasks in clients page
        # display "Deleted task" message
    elif req[0] == "OP_LOGIN":
        '''req[1] username, req[2] password'''
        get_user = '''SELECT * from users WHERE "username" = ?'''
        usr = list(cursor.execute(get_user, req[1]))
    #   if usr.empty():
    #       return error to client: wrong username, try again
    #   if usr.password != req[2](aka password)
    #       return error to client: wrong password, try again
    #   else everything ok, login
    elif req[0] == "OP_NEWUSER":
        try:
            insert_query = '''INSERT INTO users
            (name, username, password, telegram_id)
            VALUES (?, ?, ?, ?)'''
            cursor.execute(insert_query, req[1:])
            connection.commit()
        except sqlite3.Error as err:   
           print(err)
    else:
        print("Error: Unknown request")
        sys.exit()
    print_db(cursor)
    cursor.close()
    if connection:
        connection.close()

def main():
    #while True:
    #    wait for requests
    #    RequestHandler(request)
    RequestHandler(["OP_NEWUSER", "Mher", "involid", 661681731])

main()

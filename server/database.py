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
    req = req.split()
    path = os.path.abspath("database.db")
    connection = Connect(path)
    cursor = connection.cursor()
    if req[0] == "TASK_GET":
        '''req[1] user_id, req[2] date'''
        get_tasks = '''SELECT * FROM tasks WHERE "user_id" = ? "date" = ?'''
        ans = list(cursor.execute(get_tasks, req[1:]))
        # return ans to client or bot
        return ans
    elif req[0] == "TASK_ADD":
        '''(unique task_id is generated) req[1] user_id, req[2] description, req[3] date'''
        add_task = '''INSERT INTO tasks
        (user_id, description, date)
        VALUES (?, ?, ?)'''
        cursor.execute(add_task, req[1:])
        connection.commit()
        # TODO update tasks in clients page
        return ["New task added"]
    elif req[0] == "TASK_DELETE":
        '''req[1] task_id'''
        delete_task = '''DELETE from tasks WHERE "task_id" = ?'''
        cursor.execute(delete_task, req[1])
        connection.commit()
        # TODO update tasks in clients page
        return ["Deleted task"]
    elif req[0] == "OP_LOGIN":
        '''req[1] username, req[2] password'''
        get_user = '''SELECT * from users WHERE "username" = ?'''
        usr = list(cursor.execute(get_user, req[1]))
        if usr.empty():
            return ["Error: wrong username"]
        if usr.password != req[2]: #(aka password)
            return ["Error: wrong password"]
        else:
            return [usr]
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


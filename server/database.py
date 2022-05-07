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
 #   print_db(cursor)
 #   print()
    if req[0] == "TASK_GET":
        '''req[1] user_id, req[2] date'''
        get_tasks = '''SELECT * FROM tasks WHERE "user_id" = ? AND "date" = ?'''
        cursor.execute(get_tasks, (req[1], req[2]))
        all_tasks = cursor.fetchall()
        if len(all_tasks) != 0:
            return all_tasks
        else:
            return ["No Tasks"]
    elif req[0] == "GET_USERS":
        get_users = '''SELECT user_id, email FROM users'''
        cursor.execute(get_users)
        all_users = cursor.fetchall()
        return all_users
    elif req[0] == "TASK_ADD":
        date = req[-1]
        merged_description = " ".join(req[2:(len(req) - 1)])
        '''(unique task_id is generated) req[1] user_id, req[2] description, req[3] date'''
        add_task = '''INSERT INTO tasks
        (user_id, description, date)
        VALUES (?, ?, ?)'''
        cursor.execute(add_task, (req[1], merged_description, date))
        connection.commit()
        # update tasks in clients page
        cursor.execute('''SELECT * FROM tasks WHERE task_id=(SELECT max(task_id) FROM tasks)''')
        task = cursor.fetchone()
        return [task[0]]

    elif req[0] == "TASK_DELETE":
        '''req[1] task_id'''
        delete_task = '''DELETE from tasks WHERE "task_id" = ?'''
        cursor.execute(delete_task, (req[1], ))
        connection.commit()
        return []
    elif req[0] == "OP_LOGIN":
        '''req[1] username, req[2] password'''
        get_user = '''SELECT * from users WHERE "username" = ?'''
        cursor.execute(get_user, (req[1], ))
        us = cursor.fetchall()
        usr = []
        for e in us:
            usr.append(" ".join([str(val) for val in e]))
        #print(usr) 
        if len(usr) != 1:
            return ["Error: wrong username"]
        elif usr[0].split()[3] != req[2]: #(aka password)
            return ["Error: wrong password"]
        else:
            return usr[0].split()
    elif req[0] == "OP_NEWUSER":
        try:
            insert_query = '''INSERT INTO users
            (name, username, password, email)
            VALUES (?, ?, ?, ?)'''
            cursor.execute(insert_query, req[1:])
            connection.commit()
            print_db(cursor)
            return ["OK"]
        except sqlite3.Error as err:
            print_db(cursor)
            return [str(err)]
    else:
        print("Error: Unknown request")
        sys.exit()
 #   print_db(cursor)
    cursor.close()
    if connection:
        connection.close()

#RequestHandler("OP_NEWUSER Hamlet Ham_2552 hamo matevosyanhamlet9@gmail.com")
#RequestHandler("TASK_ADD 1 JAMKOCHYAN TIGRAN TIGRAN JAMKOCHYAN 2022-05-04")
#RequestHandler("TASK_ADD 1 FINISH PROJECT 2022-05-04")
#RequestHandler("OP_NEWUSER Mher Mher_787898 mher mher.karagulyan@gmail.com")
#RequestHandler("TASK_ADD 2 TODAY 22:00 MANCHESTER CITY VS REAL MADRID 2022-05-04")
#RequestHandler("TASK_ADD 2 FINISH PROJECT 2022-05-04")
#print (RequestHandler("TASK_GET 2 2022-05-07"))


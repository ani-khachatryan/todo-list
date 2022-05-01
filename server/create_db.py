import sqlite3


connect = sqlite3.connect('database.db')
connect.execute("PRAGMA foreign_keys = 1")
curs = connect.cursor()
curs.execute('''
            CREATE TABLE IF NOT EXISTS users
            ([user_id] INTEGER PRIMARY KEY NOT NULL,
            [name] TEXT,
            [username] TEXT NOT NULL UNIQUE,
            [password] TEXT NOT NULL,
            [email] TEXT NOT NULL UNIQUE)
            ''')

connect.commit()
curs.execute('''
            CREATE TABLE IF NOT EXISTS tasks
            ([task_id] INTEGER PRIMARY KEY NOT NULL,
            [user_id] INTEGER NOT NULL,
            [description] TEXT NOT NULL,
            [date] DATE NOT NULL)
            ''')

            #FOREIGN KEY([user_id]) REFERENCES users([user_id]),
connect.commit()
curs.close()
connect.close()

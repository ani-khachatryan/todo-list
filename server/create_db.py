import sqlite3


connect = sqlite3.connect('database')
curs = connect.cursor()

curs.execute('''
            CREATE TABLE IF NOT EXISTS users
            ([user_id] INTEGER NOT NULL IDENTITY PRIMARY KEY,
            [name] TEXT,
            [username] TEXT NOT NULL UNIQUE,
            [password] TEXT NOT NULL,
            [telegram_id] TEXT NOT NULL UNIQUE)
            ''')

curs.execute('''
            CREATE TABLE IF NOT EXISTS tasks
            ([task_id] INTEGER NOT NULL IDENTITY PRIMARY KEY,
            FOREIGN KEY(user_id) REFERENCES users(user_id) NOT NULL,
            [description] TEXT NOT NULL,
            [date] DATE NOT NULL)
            ''')

curs.commit()
curs.close()
connect.close()

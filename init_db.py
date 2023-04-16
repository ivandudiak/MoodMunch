import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (time, hunger) VALUES (?, ?)",
            (1, 2)
            )

cur.execute("INSERT INTO posts (time, hunger) VALUES (?, ?)",
            (3, 2)
            )

connection.commit()
connection.close()
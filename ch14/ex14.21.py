import sqlite3

conn = sqlite3.connect('testSQL.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE Book (ISBN INTEGER PRIMARY KEY NOT NULL,
            PUBLISHER TEXT,
            AUTHOR TEXT,
            PAGES  INTEGER)''')

conn.commit()
conn.close()
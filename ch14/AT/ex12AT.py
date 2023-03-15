import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Stock''')

conn.commit()
conn.close()
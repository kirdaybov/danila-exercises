import sqlite3

conn = sqlite3.connect('testSQL.db')
cur = conn.cursor()

cur.execute( 'DROP TABLE IS EXISTS Book')

conn.commit()
conn.close()
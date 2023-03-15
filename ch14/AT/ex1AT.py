import sqlite3

conn = sqlite3.connect('Stock.db')
cur = conn.cursor()

cur.execute('''SELECT * FROM Stock''')

conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''DELETE FROM Stock WHERE NumShares < 10''')

conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect('chocolate.db')
cur = conn.cursor()

cur.execute('''UPDATE Products
                SET RetailPrice = 4.99
                WHERE Description LIKE "%стружка%"''')

conn.commit()
conn.close()
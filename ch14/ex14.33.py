import sqlite3

conn = sqlite3.connect('chocolate.db')
cur = conn.cursor()

cur.execute('''DELETE FROM Products WHERE UnitCost > 4.00"''')

conn.commit()
conn.close()
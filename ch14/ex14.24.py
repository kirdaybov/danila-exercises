import sqlite3

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

cur.execute( '''INSERT INTO Inventory (ItemName, Price)
                VALUES ("Зубило", 8.99)''')

conn.commit()
conn.close()
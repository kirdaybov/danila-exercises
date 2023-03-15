import sqlite3

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

cur.execute( '''INSERT INTO Inventory (ItemID, ItemName, Price)
                VALUES (10, "Циркулярная Пила", 199.99)''')

conn.commit()
conn.close()
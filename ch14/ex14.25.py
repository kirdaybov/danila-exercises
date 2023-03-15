import sqlite3

name_input = str
price_input = float

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

cur.execute( '''INSERT INTO Inventory (ItemName, Price)
                VALUES (?,?)''', (name_input,price_input))

conn.commit()
conn.close()
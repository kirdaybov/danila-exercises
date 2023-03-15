import sqlite3

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

#Сюда вставляем варианты ниже

conn.commit()
conn.close()

#a)cur.execute( '''SELECT * FROM Inventory''')
#б)cur.execute( '''SELECT ProductName FROM Inventory''')
#в)cur.execute( '''SELECT ProductName,QtyOnHand FROM Inventory''')
#г)cur.execute( '''SELECT ProductName FROM Inventory WHERE Cost < 17.00''')
#д)cur.execute( '''SELECT * FROM Inventory WHERE ProductName LIKE "%ZZ"''')
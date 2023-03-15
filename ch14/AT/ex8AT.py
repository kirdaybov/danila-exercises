import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''INSERT INTO Stock (TradingSymbol,CompanyName,NumShares,PurchasePrice,SellingPrice)
                VALUES("XYZ", "Компания XYZ", 150, 12.55, 22.47)''')

conn.commit()
conn.close()
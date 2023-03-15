import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''SELECT TradingSymbol FROM Stock WHERE SellingPrice > PurchasePrice and NumShares > 100''')

conn.commit()
conn.close()
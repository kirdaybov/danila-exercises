import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''SELECT TradingSymbol, NumShares FROM Stock WHERE SellingPrice > PurchasePrice and NumShares > 100 ORDER BY NumShares''')

conn.commit()
conn.close()
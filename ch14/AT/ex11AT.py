import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE Stock (ItemID INTEGER PRIMARY KEY NOT NULL, TradingSymbol TEXT, CompanyName TEXT, NumShares INTEGER, PurchasePrice REAL, SellingPrice REAL)''')

conn.commit()
conn.close()
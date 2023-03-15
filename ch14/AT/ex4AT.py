import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''SELECT TradingSymbol FROM Stock WHERE PurchasePrice > 25.00''')

conn.commit()
conn.close()
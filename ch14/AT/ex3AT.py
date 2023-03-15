import sqlite3

conn = sqlite3.connect('Stock.db')
cur = conn.cursor()

cur.execute('''SELECT TradingSymbol, NumShares FROM Stock''')

conn.commit()
conn.close()
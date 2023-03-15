import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''SELECT TradingSymbol FROM Stock WHERE TradingSymbol LIKE "SU%"''')

conn.commit()
conn.close()
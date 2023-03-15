import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''UPDATE Stock SET TradingSymbol = "ABC" WHERE TradingSymbol == "XYZ"''')

conn.commit()
conn.close()
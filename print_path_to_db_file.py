import os, sqlite3
conn = sqlite3.connect("library.db")
print("DB file:", os.path.abspath("library.db"))
conn.close()
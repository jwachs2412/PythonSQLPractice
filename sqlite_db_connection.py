import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('library.db')

# Create a cursor object
cursor = conn.cursor()

# Create the Books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        BookID INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Author TEXT NOT NULL,
        Genre TEXT,
        YearPublished Integer        
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
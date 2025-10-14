import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('library.db')

# Create a cursor object
cursor = conn.cursor()

def add_book(title, author, genre, year):
    
    # Create function
    cursor.execute('''
        INSERT INTO Books (Title, Author, Genre, YearPublished)
        VALUES (?, ?, ?, ?)               
    ''', (title, author, genre, year))
    
add_book("The Martian", "Andy Weir", "Science Fiction", 2011)
    
# Commit the changes and close the connection
conn.commit()
conn.close()
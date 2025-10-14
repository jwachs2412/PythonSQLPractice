import sqlite3

def delete_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Books
        WHERE BookID = ?  
    ''', (book_id))
    conn.commit()
    conn.close()
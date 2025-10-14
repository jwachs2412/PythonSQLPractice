import sqlite3

def update_author(book_id, new_author):
    
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Books
        SET Author = ?
        WHERE BookID = ?               
    ''', (new_author, book_id))
    conn.commit()
    conn.close()
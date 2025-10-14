import sqlite3

def view_grades():
    connection = sqlite3.connect("student_grades.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM grades")
    grades = cursor.fetchall()
    for grade in grades:
        print(grade)
    connection.close()
    
view_grades()
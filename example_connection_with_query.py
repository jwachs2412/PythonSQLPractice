import pymysql

#Establish a connection to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='PythonTable'
)

#Create a cursor object
cursor = connection.cursor()

#Execute a SQL query
cursor.execute("SELECT * FROM employees")

#Fetch all rows from executed query
data = cursor.fetchall()

#Print rows of data
print(data)

#Close the connection
connection.close()
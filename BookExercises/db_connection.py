from sqlalchemy import create_engine, text

DB_USER = "root"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "To_Do_List_DB"

# Create the engine once
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
print("Engine created successfully!")

# Reusable function to execute INSERT/UPDATE/DELETE
def execute_sql(sql_query, params=None):
    """Execute a SQL statement with optional parameters."""
    with engine.connect() as connection:
        connection.execute(text(sql_query), params or {})
        connection.commit()

# Example: reusable function to insert an employee
# def insert_employee(name, position, salary):
#     sql = """
#         INSERT IGNORE INTO employees (name, position, salary)
#         VALUES (:name, :position, :salary)
#     """
#     params = {"name": name, "position": position, "salary": salary}
#     execute_sql(sql, params)
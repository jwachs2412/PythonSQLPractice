from sqlalchemy import text
from db_connection import engine, execute_sql

def add_task(description):
    sql = """
        INSERT INTO tasks (description) 
        VALUES (:description)
    """
    params = {"description": description}
    execute_sql(sql, params)
    
def view_tasks():
    sql = """
        SELECT * FROM tasks
    """
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        tasks = result.fetchall()
        
    for task in tasks:
        print(task)
    
add_task("Solve python errors")
view_tasks()
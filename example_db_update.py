from db_connection import execute_sql

loyal_employees = [101, 105, 107]

for loyal_employee_id in loyal_employees:
    
    execute_sql(
    "UPDATE employees SET loyal_employee = TRUE WHERE id = :id",
    {"id": loyal_employee_id}
)
from sqlalchemy import text
from db_connection import insert_employee

insert_employee("Jerry Dome", "Software Engineer", 75000)
insert_employee("Jake Smith", "Programmer", 80000)
insert_employee("Suzy Greenberg", "Creative Director", 120575)
print("Employee(s) added successfully!")
import pandas as pd
from example_connection_with_query import data

# Convert the fetched data into a DataFrame

df = pd.DataFrame(data, columns=['id', 'name', 'position', 'salary', 'loyal_employee'])

# Calculate total salary

total_salary = df.agg({'salary': 'sum'}).reset_index()

# Sort the summary by salary amount

salary_amount = df.sort_values(by='salary', ascending=True).head(6)

print(total_salary)
print(salary_amount)


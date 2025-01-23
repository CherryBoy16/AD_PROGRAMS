# 1 question
import pandas as pd
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}
df = pd.DataFrame(data)
print(df)


# 2 question
import pandas as pd
data = {
    'Employee_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [23, 30, 28, 35, 22],
    'Salary': [50000, 60000, 55000, 70000, 45000]
}
df = pd.DataFrame(data)
print("First 2 rows of the DataFrame:")
print(df.head(2))
df['Bonus'] = df['Salary'] * 0.10
average_salary = df['Salary'].mean()
print("\nAverage Salary of employees:", average_salary)
filtered_df = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(filtered_df)
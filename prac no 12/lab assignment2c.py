import pandas as pd
df_employee = pd.read_excel('employee.xlsx')
developers = df_employee[df_employee['Designation'].str.contains('Developer', case=False, na=False)]
print("List of all Developers:")
print(developers[['Employee ID', 'Employee Name', 'Department', 'Designation']])
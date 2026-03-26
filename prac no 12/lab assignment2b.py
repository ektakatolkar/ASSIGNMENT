import pandas as pd
df_employee = pd.read_excel('employee.xlsx')
automotive_employees = df_employee[df_employee['Domain'] == 'Automotive']
print("Employees working in Automotive domain:")
print(automotive_employees[['Employee ID', 'Employee Name', 'Department', 'Designation']])
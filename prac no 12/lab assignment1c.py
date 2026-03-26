import pandas as pd
df = pd.read_csv('diamonds.csv')
avg_x = df['x'].mean()
avg_y = df['y'].mean()
avg_z = df['z'].mean()
print(f"Average of x is : {avg_x:.2f}")
print(f"Average of y is : {avg_y:.2f}")
print(f"Average of z is : {avg_z:.2f}")
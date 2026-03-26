import pandas as pd
import matplotlib.pyplot as plt

data = {
    'month_number': [1,2,3,4,5,6,7,8,9,10,11,12],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1550,1120,1400,1780,1890,2100,1760]
}

df = pd.DataFrame(data)

width = 0.4

plt.bar(df['month_number'], df['facecream'], 
        width=width, color='orange', label="Face Cream")

plt.bar(df['month_number'], df['facewash'], 
        width=width, color='purple', label="Face Wash", alpha=0.7)

plt.legend()
plt.title("Face Cream and Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
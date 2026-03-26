import pandas as pd
import matplotlib.pyplot as plt

data = {
    'month_number': [1,2,3,4,5,6,7,8,9,10,11,12],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1550,1120,1400,1780,1890,2100,1760],
    'toothpaste': [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
}

df = pd.DataFrame(data)

plt.plot(df['month_number'], df['facecream'], 
         label="Face Cream", color='pink', marker='o')

plt.plot(df['month_number'], df['facewash'], 
         label="Face Wash", color='blue', marker='s')

plt.plot(df['month_number'], df['toothpaste'], 
         label="Toothpaste", color='green', marker='^')

plt.legend()
plt.title("Sales Data")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.grid(True)
plt.show()
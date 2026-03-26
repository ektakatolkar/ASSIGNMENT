import pandas as pd
import matplotlib.pyplot as plt

data = {
    'month_number': [1,2,3,4,5,6,7,8,9,10,11,12],
    'total_profit': [211000,183300,224700,257500,265200,234000,266000,282000,295000,300000,310000,330000]
}

df = pd.DataFrame(data)

plt.plot(df['month_number'], df['total_profit'], 
         color='teal', marker='o', linewidth=2)

plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid(True)
plt.show()
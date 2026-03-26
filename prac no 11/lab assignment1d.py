import pandas as pd
import matplotlib.pyplot as plt

data = {
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1550,1120,1400,1780,1890,2100,1760],
    'toothpaste': [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
}

df = pd.DataFrame(data)

fc = df['facecream'].sum()
fw = df['facewash'].sum()
tp = df['toothpaste'].sum()

labels = ['Face Cream', 'Face Wash', 'Toothpaste']
values = [fc, fw, tp]

colors = ['#ff9999', '#66b3ff', '#99ff99']

plt.pie(values, labels=labels, colors=colors)

plt.title("Total Sales Distribution")
plt.show()
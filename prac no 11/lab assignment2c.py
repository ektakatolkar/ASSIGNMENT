import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Amdocs']
recruitments = [50, 60, 55, 40, 35]

colors = ['#ff6666','#3399ff','#99ff99','#ffcc66','#9966cc']

plt.pie(recruitments, labels=companies, colors=colors)
plt.title("Customized Pie Chart")
plt.show()
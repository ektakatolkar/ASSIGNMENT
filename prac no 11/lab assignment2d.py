import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Amdocs']
recruitments = [50, 60, 55, 40, 35]

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.pie(recruitments, labels=companies, colors=colors)
centre_circle = plt.Circle((0,0), 0.70, fc='white')  
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Doughnut Chart of Recruitments")
plt.show()
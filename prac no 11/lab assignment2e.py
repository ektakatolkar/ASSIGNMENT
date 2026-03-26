import matplotlib.pyplot as plt

companies = ['IBM', 'Amdocs']
recruitments = [40, 35]

colors = ['#3399ff','#ff6666']

plt.bar(companies, recruitments, color=colors, width=0.4)
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Number of Students")
plt.grid(axis='y')

plt.show()
import matplotlib.pyplot as plt
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Amdocs']
recruitments = [50, 60, 55, 40, 35]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
width = 0.5
plt.bar(companies, recruitments, color=colors, width=width)
plt.title("Recruitments in Companies")
plt.xlabel("Company")
plt.ylabel("Number of Students")
plt.grid(axis='y')
plt.show()
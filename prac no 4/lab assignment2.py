import numpy as np

m1 = []
for i in range(5):
    row = list(map(int, input().split()))
    m1.append(row)

m2 = []
for i in range(3):
    row = list(map(int, input().split()))
    m2.append(row)

m1 = np.array(m1)
m2 = np.array(m2)

result = np.dot(m1, m2)
print(result)
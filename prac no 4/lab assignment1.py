import numpy as np

identity_matrix = np.eye(4)
print(identity_matrix)

a = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 3))

print(a)
print(b)
print(a + b)
print(np.dot(a, b))
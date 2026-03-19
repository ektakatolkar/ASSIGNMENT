file1 = open("input.txt", "r")
data = file1.read()
file1.close()

upper_data = data.upper()

file2 = open("output.txt", "w")
file2.write(upper_data)
file2.close()

print("Original Content:")
print(data)

print("\nUppercase Content Written to New File:")
print(upper_data)
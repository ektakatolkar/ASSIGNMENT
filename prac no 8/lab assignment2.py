source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

file1 = open(source, "r")
file2 = open(destination, "w")

for line in file1:
    text = line.strip()
    if text != "" and not text.startswith("#"):
        file2.write(line)

file1.close()
file2.close()

print("\nSource File Content:")
file1 = open(source, "r")
print(file1.read())
file1.close()

print("\nDestination File Content:")
file2 = open(destination, "r")
print(file2.read())
file2.close()
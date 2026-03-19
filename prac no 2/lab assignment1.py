v = float(input("Enter voltage: "))
r = float(input("Enter resistance: "))

current = v / r
print("Current =", current)

if current < 0.5:
    print("Low current")
elif current <= 2:
    print("Normal current")
else:
    print("High current")
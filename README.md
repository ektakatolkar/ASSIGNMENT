# ASSIGNMENT 01
numbers = tuple(map(int,input("Enter integers separated by space: ") split()))
print("Total number of items : ",len(numbers))
print("last item:",numbers[-1])
print("Reverse order:",numbers[::-1])
if 5 in numbers:
print("yes,5 is present")
else:
print("No,5 is not present")
new_tuple=numbers[1:-1]
print("After removing first and last item:",new_tuple)
  

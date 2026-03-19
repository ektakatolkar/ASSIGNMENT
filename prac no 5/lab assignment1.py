numbers = tuple(map(int, input().split()))

print("Total number of items:", len(numbers))
print("Last item:", numbers[-1])
print("Tuple in reverse order:", numbers[::-1])

if 5 in numbers:
    print("Yes")
else:
    print("No")

if len(numbers) > 2:
    new_tuple = numbers[1:-1]
    print("Sorted tuple:", tuple(sorted(new_tuple)))
else:
    print("Not enough elements")
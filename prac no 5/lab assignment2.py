prices = tuple(map(int, input().split()))

print("Total items sold:", len(prices))
print("Cheapest item price:", min(prices))
print("Costliest item price:", max(prices))
print("Prices in ascending order:", tuple(sorted(prices)))
print("Number of costliest items sold:", prices.count(max(prices)))
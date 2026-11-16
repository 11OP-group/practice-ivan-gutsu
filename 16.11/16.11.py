prices = [100,50, 200, 150]
print("Дорогой:",max(prices))
print("Дешевый:",min(prices))

average= sum(prices) / len(prices)
print(average)

print(*prices, sep= ",")
price = int(input())
coin = 0

while price >0:
    if price >= 25:
        price = price - 25
    elif price >= 10 :
        price = price -10
    elif price >=5:
        price = price - 5
    else:
        price = price -1
    coin = coin + 1
print(f"{coin}")

DISCOUNT = 0.9
basket = 0

while True:
    price = int(input("Введите цену товара:"))
    if price == 0:
        break
    if price < 0:
        print("Ошибка цены")
        continue
    basket += price

if basket >1000:
    basket = basket * DISCOUNT

print(f"Полная стоимость корзины . с учетом скидки если есть {basket}")
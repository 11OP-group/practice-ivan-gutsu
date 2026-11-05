high_number = 0
while True:
    number = int(input("Введите натуральное число:"))
    if number == 0:
        break
    elif number > high_number:
        high_number = number
print(high_number)
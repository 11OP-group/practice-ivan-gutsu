number_1 = int(input ("Введите первое число: "))
number_2 = int (input("Введите второе число: "))
while True:
    if number_2 <= number_1:
        print("Ошибка. Введите число побольше, чем первое")
        number_2 = int (input ("Введите второе число: "))
    else:
        break

number_3 = int (input("Введите третье число: "))
while True:
    if number_3 <= number_2:
        print("Введите число побольше, чем второе")
        number_3 = int(input("Введите третье число: "))
    else:
        break
print ("Последовательность принята!")
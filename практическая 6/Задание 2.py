number = int(input())
if number <0  or number >36:
    print(f"ОШИБКА ВВОДА ")

elif number == 0 :
    print(f"Зеленый")

elif (1<=number<=10 or 19<=number<=28) and number% 2 ==1:
    print(f"Красный")

elif (1<=number<=10 or 19<=number<=28) and number%2 ==0:
    print(f"Черный")

elif (11<=number<=18 or 29<=number<=36) and number%2 ==1:
    print(f"Черный")
else:
    print(f"Красный")
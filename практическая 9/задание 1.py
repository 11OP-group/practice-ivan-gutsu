n = int(input("Введите число"))

number =  1
while number <= n:
    if number < 5 or  9 < number < 17 or  37 < number <  78  or  number > 87:
        print(f"{number}")
    number = number + 1

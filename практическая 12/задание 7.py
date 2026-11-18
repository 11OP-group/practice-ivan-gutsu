numbers = [10, 20, 30, 40, 50]
n = int(input("введите число:"))
found = False

for i in range(len(numbers)):
    if numbers[i] == n:
        print("found")
        found = True
        break
       
if not found:
    print("Нет такого числа")
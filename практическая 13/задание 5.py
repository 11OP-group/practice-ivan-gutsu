text = input("Введите числа: ")
numbers = text.split()

para = 0
for i in range(len(numbers)):
    for h in range( i +1, len(numbers)):
        if numbers[i] == numbers[h]:
             para = para + 1
print(para)
text = input("Введите числа: ")
numbers = text.split()

para = 0
for i in range(len(numbers)- 1 ):
        if numbers[i] == numbers[i + 1]:
             para = para + 1
print(para)
n = int(input("Введите количество чисел:"))

MAX = 0
MAX2 = 0

print("введите сами числа ")

for i in range(n):
    number = int(input())
    if number > MAX:
        MAX2 = MAX
        MAX = number
    else:
        if number > MAX2:
            MAX2 = number

print(f"Наибольшее число: {MAX}")
print(f"Второе наибольшее: {MAX2}")
n = int(input())

last = n % 10
count3= 0
count_last= 0
count_even= 0
summ = 0
product= 1
count05= 0

while n >0:
    number = n % 10
    if number == 3:
        count3 = count3 + 1
    if number == last:
        count_last = count_last + 1
    if number % 2 == 0:
        count_even = count_even +1
    if number > 5:
        summ = summ + number
    if number > 7:
        product= product * number
    if number == 0 or number == 5:
        count05 = count05 + 1
    n = n // 10
print(f"{count3}")
print(f"{count_last}")
print(f"{count_even}")
print(f"{summ}")
print(f"{product}")
print(f"{count05}")


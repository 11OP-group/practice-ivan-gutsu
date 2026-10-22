n = int(input())
summa = 0
for i in range(1, n + 1 ):
    if i % 2 == 1:
        summa = summa + i
    else:
        summa = summa - i

print(summa)
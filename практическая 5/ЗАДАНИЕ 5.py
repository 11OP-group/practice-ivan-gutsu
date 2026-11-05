summa = int(input("Введите сумму которую хотите снять "))
remainder = summa

count_5000 =remainder  // 5000
remainder = remainder % 5000

count_2000 = remainder // 2000
remainder = remainder % 2000

count_1000 = remainder // 1000
remainder = remainder % 1000

count_500 = remainder // 500
remainder = remainder % 500

count_200 = remainder // 200
remainder = remainder % 200

count_100 = remainder // 100
remainder = remainder % 100

print(f"5000 руб :.{count_5000} шт")
print(f"2000 руб :.{count_2000} шт")
print(f"1000 руб :.{count_1000} шт")
print(f"500 руб :.{count_500} шт")
print(f"200 руб :.{count_200} шт")
print(f"100 руб :.{count_100} шт")
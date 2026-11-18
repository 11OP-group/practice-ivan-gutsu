import  random

marks = []
for i in range(10):
    marks.append(random.randint(2, 5))
count_5= 0
count_2 =0

for i in marks:
    if i ==5 :
        count_5 += 1
    elif  i == 2:
        count_2 += 1

print(f"Количество пятерок:  {count_5}")
print(f"Количество двоек: {count_2}")


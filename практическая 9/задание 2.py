found  = False
people  = 0

while True:
    name = input("Введите имя ")
    if name == "Александра":
        found = True
    elif  name == "Левон":
        break
    elif found:
        people = people +1
print(people)

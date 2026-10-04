student = {} # Создали словарь
name = input(" Ваше имя : ")
age_str = input(" Ваш возраст : ")
sub_str = input(" Любимые предметы : ")

student = {
    'name': name,
    'age': age,
    'sub': sub_str
}


print('=' * 30)
print('АНКЕТА СТУДЕНТА')
print('=' * 30)

print("Имя:", student['name'])
print("Возраст:", student['age'])
print("Любимые предметы:", {student['sub'])

print('=' * 30)

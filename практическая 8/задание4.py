population = int(input()) # старт кол организм
percent = int(input()) # увеличение в процент
days = int(input()) # кол дней для размножения

for i in range(1, days + 1):
    population = population +  population * percent/ 100
    print(days , population)


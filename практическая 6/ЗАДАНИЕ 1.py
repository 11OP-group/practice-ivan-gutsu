temperature = float(input("Температура: "))
pressure = float(input("Давление:"))
pulse = float(input("Пульс:"))
if temperature <35 or temperature > 38 or pressure < 105 or pressure > 140 or pulse <55 or pulse >110 :
    print(f"Требуется врач ")
elif temperature <36 or temperature>37 or pressure <110 or pressure>130 or pulse<60 or pulse<110:
    print(f"Легкое недомогание ")
else:
    print(f"Нормальное состояние ")

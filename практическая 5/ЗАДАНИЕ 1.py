income=float(input("Введите годовой доход:"))
tax_rate = 0.13
tax = income * tax_rate
hand =income - tax

print(f"Общая сумма дохода: {income:.2f} руб".replace(",", " "))
print(f"Сумма рассчитанного налога: {tax:.2f} руб".replace(",", " "))
print(f"Сумма на руках после вычета налога: {hand:.2f} руб ".replace(",", " "))
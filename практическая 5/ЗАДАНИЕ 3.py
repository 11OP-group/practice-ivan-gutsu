USD_TO_RUB = 95.50

def convert_USD_TO_RUB(amount_usd):

    return amount_usd * USD_TO_RUB

text = input("Введите сумму в долларах: ")
amount_usd = float(text)

amount_rub = convert_USD_TO_RUB(amount_usd)

print(f"{amount_usd:.2f} = {amount_rub:.2f} руб.")






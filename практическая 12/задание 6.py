word = input().lower()

letter = list(word)
name = letter[::-1]


if letter == name:
    print("Это палиндром")
else:
    print("Не палиндром")

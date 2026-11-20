found = False

for a in range(1,151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                summa = a**5 + b**5 + c**5 + d**5
                e =round(summa ** (1/5))

                if e >150:
                    continue
                if e**5 == summa and e > d:
                    print(a,b,c,d,e)
                    print(f"{a + b + c + d + e}")
                    found = True
                    break
                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print("нет решения")
def padezsh(num):
    if num >= 11 and num <=20:
        return str(num) + " рублей"
    a = num % 10
    if a == 1:
        return str(num) + " рубль"
    elif a > 1 and a <5:
        return str(num) + " рубля"
    elif a > 4 or a == 0 :
        return str(num) + " рублeй"

c = int(input("Введите число:\n"))
result = padezsh(c)
print(result)
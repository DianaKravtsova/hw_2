def rubli(num):
    if num >= 11 and num <=20:
        return  " рублей "
    a = num % 10
    if a == 1:
        return  " рубль "
    elif a > 1 and a <5:
        return  " рубля "
    elif a > 4 or a == 0 :
        return " рублeй "

def cent(num):
    if num >= 11 and num <=20:
        return  " копеек "
    a = num % 10
    if a == 1:
        return  " копейка "
    elif a > 1 and a <5:
        return  " копейки "
    elif a > 4 or a == 0 :
        return " копеек "

def number(value):
    arr1 = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    arr2 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    arr3 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    arr4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    sotni = value//100
    result = ""
    if sotni != 0:
        result = result + arr4[sotni - 1] + " "
        value %= 100
    if value < 10:
        result = result + arr1[value] + " "
    if value >= 10 and value <= 19:
        result = result + arr2[value] + " "
    if value >=20 and value <= 99:
        desyatki = value // 10
        result = result + arr3[desyatki-2] + " "
        ed = value % 10
        if ed != 0:
            result = result + arr1[ed] + " "

    return result

def out(num):
    b = num.split(',')

    r = int(b[0])
    c = int(b[1])

    return number(r) + rubli(r) + number(c) + cent(c)

a = input("Введите число: ")
res = out(a)
print("Результат:" + res)


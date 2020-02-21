def number(value):
    arr1 = ["ноль", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    arr2 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    arr3 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    arr4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    sotni = value//100
    result = ""
    if sotni != 0:
        result = result + arr4[sotni - 1] + " "
        value %= 100
    if value < 10:
        result = result + arr1[value]
    if value >= 10 and value <= 19:
        result = result + arr2[value] + " "
    if value >=20 and value <= 99:
        desyatki = value // 10
        result = result + arr3[desyatki-2] + " "
        ed = value % 10
        if ed != 0:
            result = result + arr1[ed] + " "

    return result

a = int(input("Введите число: "))
res = number(a)
print("Результат: " + str(res))


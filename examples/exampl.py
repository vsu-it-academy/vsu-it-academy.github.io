chislo = 1
summa = 0
kol = 0

while chislo != 0:
    chislo = int(input("Введите число: "))
    kol+=1
    summa+=chislo
print("Количество введеных чисел: ", kol)
print("Сумма введеных чисел: ", summa)

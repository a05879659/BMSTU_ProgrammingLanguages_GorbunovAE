from math import *
from random import *

n = int(input("Введите число элементов N:"))
mas = []

for i in range(n):
    mas.append(randint(-10, 10))
    maxa = mas.index(max(mas))
    z = [i for i, x in enumerate(mas) if x == 0]
    if len(z) >= 2:
        mul = 1
        for i in range(z[0] + 1, z[1]):
            mul *= mas[i]
    else: mul = "Недостаточное количесство нулей"

print(mas)
nechet = mas[::2]
chet = mas[1::2]
mas = nechet + chet

print("Номер максимального элемента массива:", maxa)
print("Произведение элементов массива между двумя первыми нулями:", mul)
print(mas)
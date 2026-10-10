from math import *
import numpy as np

def MakeMatr(n, a, b):
    Matr = (b-a)*np.random.random(size=(n, n))+a
    return Matr

def PrintMatr(Matr):
    (nRow, nCol) = Matr.shape
    for Row in range(nRow):
        for Col in range(nCol):
            print("{0: 7.3f}".format(Matr[Row][Col]), end=" ")
        print()
    print()

MyMatr = MakeMatr(8, -10, 10)
PrintMatr(MyMatr)
flag = False

for k in range(8):
    column = [MyMatr[i][k] for i in range(8)]

    if np.array_equal(MyMatr[k], column):
        print("k =", k + 1)
        flag = True
if not flag:
    print("k не найдено")

summa = 0
for i in range(8):
    if any(x < 0 for x in MyMatr[i]):
        summa += sum(MyMatr[i])

print("Сумма строк с отрицательными элементами:", summa)
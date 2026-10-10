from math import *

a = float(input('Введите переменную "a":'))

z1 = (cos((3/8*pi)-a/4))**2-(cos((11/8*pi)+a/4))**2
z2 = sqrt(2)/2*sin(a/2)
print("Z1={:.2f}, Z2={:.2f}".format(z1, z2))
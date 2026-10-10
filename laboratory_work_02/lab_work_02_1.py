from math import *

x = float(input("Введите значение X:"))

if x < -3: y=3
if -3 <= x <= 3: y=3-sqrt(9-x**2)
if 3 < x <= 6: y=-2*x+9
if 6 < x: y=x-9

print("X={:.2f}, Y={:.2f}".format(x, y))
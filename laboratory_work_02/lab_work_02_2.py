from math import *
x = float(input("Введите значение X:"))
y = float(input("Введите значение Y:"))
r = float(input("Введите значение R:"))
flag = 0

if ((-2*r <= x <= 0) and ((y<=r+sqrt(r**2-(x+r)**2)) and y>=r-sqrt(r**2-(x+r)**2))) or ((0 < x <= 2*r) and (-r <= y < 0)): flag = 1
else: flag = 0

print("Точка X={:.2f}, Y={:.2f}, R={:.2f}".format(x, y, r))
if flag: print("Попадает в область")
else: print("Не попадает в область")

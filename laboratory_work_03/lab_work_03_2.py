from math import *
from random import *
flag = 0

r = float(input("R="))
print("     X       Y    Res  R={:.2f}".format(r))
print("-------------------------------")
for n in range(10):
    x = uniform(-2*r, 2*r)
    y = uniform(-r, 2*r)
    if ((-2*r <= x <= 0) and ((y<=r+sqrt(r**2-(x+r)**2)) and y>=r-sqrt(r**2-(x+r)**2))) or ((0 < x <= 2*r) and (-r <= y < 0)): flag = 1
    else: flag = 0
    print("{: 7.2f} {: 7.2f}".format(x, y), end="   ")
    if flag: print("Yes")
    else: print("No")
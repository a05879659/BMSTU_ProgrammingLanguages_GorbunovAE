from math import *
xb = float(input("Xbeg ="))
xe = float(input("Xend ="))
dx = float(input("Dx ="))
eps = float(input("Eps="))
print("+-------+--------+------+")
print("I   X   I   Y    I   N  +")
print("+-------+--------+------+")
xt = xb
while xt <= xe:
    an = xt
    n = 0
    y = an
    while True:
        k=(-(xt**2)*(2*n+1))/(2*n+3)
        an = an*k
        y += an
        n += 1
        if abs(an) < eps: break
        print("I{: 6.2f} I {: 6.2f}  I{: 3d}  I".format(xt, y, n))
        xt += dx
print("+-------+--------+------+")
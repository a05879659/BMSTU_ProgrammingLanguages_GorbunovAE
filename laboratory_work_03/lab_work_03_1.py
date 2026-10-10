from math import *
xb = float(input("Xbeg ="))
xe = float(input("Xend ="))
dx = float(input("Dx ="))

print("Xbeg={:.2f} Xend={:.2f}".format(xb, xe))
print("     Dx={:.2f}".format(dx))
xt = xb
print("+-------+--------+")
print("I   X   I   Y    I")
print("+-------+--------+")
while xt <= xe:
    if xt < -3: y=3
    if -3 <= xt <= 3: y=3-sqrt(9-xt**2)
    if 3 < xt <= 6: y=-2*xt+9
    if 6 < xt: y=xt-9
    print("I{: 6.2f} I{: 6.2f}  I".format(xt, y))
    xt += dx
print("+-------+--------+")
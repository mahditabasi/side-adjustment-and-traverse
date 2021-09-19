import numpy as np
import math
p = math.pi

m = int(input("Number of side: "))



angel = list(map(float, input("angels: ").split(' ')[:m]))
f_angel = ((np.sum(angel)) - ((2 * m) - 4) * 90)

print(f_angel)

c_angel = (-1 * f_angel) / m
g = int(input("NUMBER OF couple: "))
gg = float(input("Device error: "))
ggg = (2.5 * gg * np.sqrt(len(angel) / g))
if f_angel <= ggg:
    angel2 = []
    for i in range(0,m):
        s = angel[i] + c_angel
        angel2.append(s)
    print(angel2)
else:
    print("ERROR")


side = list(map(float, input("Lengh of side: ").split(' ')[:m]))
g5 = float(input("First gisement: "))
ng = int(input("Number of gisements: "))
gisement = []
gisement.append(g5)

for i in range(0,ng - 1):
    g = angel[i] + gisement[i] + 100
    gisement.append(g)


rad_gisement = []
for i in range(0, len(gisement)):
    b = np.deg2rad(gisement[i])
    rad_gisement.append(b)
print(gisement)


e = []
for i in range(0,m):
    e1 = (side[i] * np.sin(rad_gisement[i]))
    e.append(e1)
n = []
for i in range(0,m):
    n1 = side[i] * np.cos(rad_gisement[i])
    n.append(n1)
f_e = np.sum(e)
f_n = np.sum(n)
f = np.sqrt(np.power(f_e, 2) + np.power(f_n, 2))
print(f)
f_g = (np.arctan(f_e / f_n) * 180 / p)
print(f_g)
l = np.sum(side)
print(l)
error_r = f / l
print(error_r)
o = float(input("Device error: "))
error_max = (2.5 * o) * (np.sqrt(2) / 4) * (np.sum(side)) * (np.sqrt(m / 2))
if f <= error_max:
    xx = []
    yy = []
    for i in range(0,m):
        c_x = ((-1 * f_e) / l) * side[i]
        xx.append(c_x)
        c_y = ((-1 * f_n) / l) * side[i]
        yy.append(c_y)
    side_x = [1000]
    side_y = [1000]
    for j in range(0,m - 1):
        v = side_x[j] + e[j] + xx[j]
        side_x.append(v)
        vv = side_y[j] + n[j] + yy[j]
        side_y.append(vv)
    print(side_x)
    print(side_y)
else:
    print("ERROR")
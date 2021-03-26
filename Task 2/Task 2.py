from math import sqrt
from csv import *
import time


coor = [[0]*3 for i in range(3)]

radius1 = log.find("radius") + 8
radius = float(log[radius1: log.find("}", radius1)])
for i in range(3):
    if i == 0:
        ind = log.find("center") + 9
        i2 = log.find("]", ind)
    else:
        ind = log.find("line") + 8
        i2 = log.find("]", ind)
        if i == 2:
            ind = i2 + 4
            i2 = log.find("]", ind)
    coords = " " + log[ind: i2] + ","
    
    ind = 0
    for x in range(3):
        c1 = coords.find(",", ind) + 1
        coor[i][x] = float(coords[ind + 1: c1 - 1])
        ind = c1

a = (coor[2][0] - coor[1][0])*(coor[2][0] - coor[1][0]) + (coor[2][1] - coor[1][1])*(coor[2][1] - coor[1][1]) + (coor[2][2] - coor[1][2])*(coor[2][2] - coor[1][2])
b = -2 * ((coor[2][0] - coor[1][0])*(coor[0][0] - coor[1][0]) + (coor[2][1] - coor[1][1])*(coor[0][1] - coor[1][1]) + (coor[0][2] - coor[1][2])*(coor[2][2] - coor[1][2]))
c = (coor[0][0] - coor[1][0])*(coor[0][0] - coor[1][0]) + (coor[0][1] - coor[0][0])*(coor[0][1] - coor[1][1]) + (coor[0][2] - coor[1][2])*(coor[0][2] - coor[1][2]) - radius*radius

d = b*b - 4 * a * c

if d < 0:
	print("Коллизий не найдено")
elif d == 0:
    t = b/(2*a)
    x1 = coor[1][0] + (coor[2][0] - coor[1][0])*t
    y1 = coor[1][1] + (coor[2][1] - coor[1][1])*t
    z1 = coor[1][2] + (coor[2][2] - coor[1][2])*t
    print(x1, y1, z1)


elif d > 0:
    t = (-b + sqrt(d))/(2*a)
    t1 = (-b - sqrt(d))/(2*a)

    x1 = coor[1][0] + (coor[2][0] - coor[1][0])*t
    y1 = coor[1][1] + (coor[2][1] - coor[1][1])*t
    z1 = coor[1][2] + (coor[2][2] - coor[1][2])*t
    print(x1, y1, z1)

    x2 = coor[1][0] + (coor[2][0] - coor[1][0])*t1
    y2 = coor[1][1] + (coor[2][1] - coor[1][1])*t1
    z2 = coor[1][2] + (coor[2][2] - coor[1][2])*t
    print(x2, y2, z2)


print('Консоль закроется через 20 секунд...')
time.sleep(20)
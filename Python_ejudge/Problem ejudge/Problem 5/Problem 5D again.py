def max (point1,point2):
    if point1 > point2:
        return point1
    else:
        return point2

def min (point1,point2):
    if point1 > point2:
        return point2
    else:
        return point1

point = int(input())
coor1 = str(input())

xmax = int(coor1.split()[0])
xmin = int(coor1.split()[0])
ymax = int(coor1.split()[1])
ymin = int(coor1.split()[1])

for i in range(0,point-1):
    coor2 = str(input())
    xmax = max(xmax,int(coor2.split()[0]))
    xmin = min(xmin,int(coor2.split()[0]))
    ymax = max(ymax,int(coor2.split()[1]))
    ymin = min(ymin,int(coor2.split()[1]))
side1 = xmax - xmin
side2 = ymax - ymin
if side1 > side2:
    side = side1
else:
    side =side2
print(side**2)
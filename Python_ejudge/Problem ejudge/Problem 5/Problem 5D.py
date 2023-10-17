def max (point1,point2):
    if point1 > point2:
        max = point1
        return max
    else:
        max = point2
        return max
    

def min (point1,point2):
    if point1 > point2:
        min = point2
        return min
    else:
        min = point1
        return min

point = int(input())
coor1 = str(input())
maxX = int(coor1.split()[0])
minX = int(coor1.split()[0])
maxY = int(coor1.split()[1])
minY = int(coor1.split()[1])

for i in range(point-1):
    coor2 = str(input())
    maxX = max(maxX,int(coor2.split()[0]))
    minX = min(minX,int(coor2.split()[0]))
    maxY = max(maxY,int(coor2.split()[1]))
    minY = min(minY,int(coor2.split()[1]))


xmax_xmin = maxX - minX
ymax_ymin = maxY - minY

if xmax_xmin > ymax_ymin :
    side = xmax_xmin
else:
    side = ymax_ymin
print(side**2)
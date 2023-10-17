xa1 = int(input())
ya1 = int(input())
xa2 = int(input())
ya2 = int(input())
xb1 = int(input())
yb1 = int(input())
xb2 = int(input())
yb2 = int(input())

# find right which is the most left side
if xb2 > xa2 :
    right = xa2
else:
    right = xb2

# find left which is the most right side
if xa1 < xb1 :
    left = xb1
else :
    left = xa1

# find top which is the most bottom side
if ya1 > yb1 :
    top = yb1
else :
    top = ya1
# find bottom which is the most top side
if ya2 > yb2 :
    bottom = ya2
else : 
    bottom = yb2

# overlap or not

if top > bottom and right > left :
    width = right-left
    height = top-bottom
    print(width*height)
else :
    print(0)
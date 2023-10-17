XA1 = int(input())
YA1 = int(input())
XA2 = int(input())
YA2 = int(input())
XB1 = int(input())
YB1 = int(input())
XB2 = int(input())
YB2 = int(input())

#Left that most right
if XA1 > XB1:
    left = XA1
else:
    left = XB1

#Right that most left
if XA2 > XB2:
    right = XB2
else:
    right = XA2

#Top that most low
if YA1 > YB1:
    top = YB1
else:
    top = YA1

#Bottom that most high
if YA2 > YB2:
    bottom = YA2
else:
    bottom = YB2

#compare ว่าทับกันมั้ย
if right > left and top > bottom:
    width = right-left
    height = top-bottom
    print(width*height)
else:
    print(0)
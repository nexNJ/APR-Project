min = 0
#9 4 5
#4 9 5
def min(x,y,z):
    min = x
    if x > y:
        min = y
        if z > y:
            min = y
        else:
            min = z
    elif x < y:
        min = x
        if x > z:
            min = z
        else:
            min = x
    return min
        
a = int(input())
b = int(input())
c = int(input())
print(min(a,b,c))
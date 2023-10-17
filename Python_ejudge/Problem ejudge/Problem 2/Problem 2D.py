x =int(input())
y =int(input())
z =int(input())

if x>y:
    if x>z:
        print(z)
    else:
        print(x)          
if x<y:
    if y>z:
        print(z)
    else:
        print(y)
else:
    if x==y:
        print(x)
    elif x==z:
        print(x)
    elif y==z:
        print(y)   

def is_same(a,b):
    for _ in range(len(b)):
        if a == b:
            return True
        else:
            b = b[1:] + [b[0]]

    b.reverse()

    for _ in range(len(b)):
        if a == b:
            return True
        else:
            b = b[1:] + [b[0]]
    

x = [__ for __ in input().split()]
y = [__ for __ in input().split()]

print("same" if is_same(x,y) else"diff")




result = None
x = [x for x in input().split()]
y = [y for y in input().split()]

for i in range(len(y)):
    if x == y:
        result = True
        break
    else:
        y = y[1:] + [(y[0])]

# return to old value(y)
y.reverse()
# reversed

for i in range(len(y)):
    if x == y:
        result = True
        break
    else:
        y = y[1:] + [(y[0])]

if result == None:
    print("different")
else:
    print("same")
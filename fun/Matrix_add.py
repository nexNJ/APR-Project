r =int(input("enter rows"))
c =int(input("enter colums"))
a =[]
for i in range(r):
    t = []
    for j in range(c):
        val = int(input(f'enter a [{i}][{j}]: '))
        t.append(val)
    a.append(t )
t =int(input("enter rows"))
g =int(input("enter colums"))

b =[]
for i in range(t):
    v = []
    for j in range(g):
        val = int(input(f'enter b [{i}][{j}]: '))
        v.append(val)
    b.append(v )
print(a)
print(b)


result= []
for i in range(r):
    p = []
    for j in range(c):
        val = 0
        p.append(val)
    result.append(p)

for i in range(len(a)):
    for j in range(len(b)):
        result[i][j] = a[i][j] + b[i][j]
print(result)

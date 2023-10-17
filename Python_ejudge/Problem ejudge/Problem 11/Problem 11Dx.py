
p = []
r = 0
while True:
    x = input()
    if x =="$":
        break
    p.append(int(x))
m = p[0]

if len(p) == 1:
    if int(m) > 0 :
        print(0)
    else:
        print(abs(m))
#case 1
else:
    if len(p) == 2:
        if p[0]<0:
            print(abs(p[0]))
        else:
            print(0)
    else:
        w = []
        r = p[0]
        for i in range(1,len(p)):
            r += p[i]
            if r < 0 :
                w.append(r)
        h = p[0]
        if h < r:
            print(abs(h))
        else:
            print(abs(min(w))) 





    


p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

ans = []
Nex = []
for i in range(len(q)):
    count = 0
    for j in range(len(p)):
        if count == 0:
            x = q[i] * p[j]
            ans.append(x)
        else:
            x = q[i] * p[j]
            Nex.append(x)
print(ans,Nex)
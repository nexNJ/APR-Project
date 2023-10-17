p = input().split()
q = input().split()

ans = []

for a in range(len(q)):
    count = 0
    for b in range(len(p)):
        if a == 0:
            x = int(q[a]) * int(p[b])
            ans.append(x)
        else:
            if count + a == len(ans):
                x = int(q[a]) * int(p[b])
                ans.append(x)
            else:
                x = int(q[a]) * int(p[b])
                ans[count+a] = ans[count+a] + x
                count += 1

for c in ans:
    print(c, end=' ')
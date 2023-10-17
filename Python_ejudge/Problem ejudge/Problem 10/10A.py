x =int(input())

for i in range(x):
    y = input().split()
    if i ==0:
        a = set(y)
    else:
        a = a.intersection(set(y))
print(a)

real_ans = list(a)
real_ans.sort()

if len(real_ans) == 0:
    print("Notthing")
else:
    print(real_ans)
for k in real_ans:
    print(k,end=" ")
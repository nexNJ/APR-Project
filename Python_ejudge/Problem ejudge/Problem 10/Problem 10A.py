'''people = int(input())

for i in range(people):
    x = input().split()
    if i ==0:
        result = set(x)
    else:
        result =  result.intersection(set(x))
result = list(result)
result.sort()

if len(result) == 0:
    print("Nothing")
else:
    for j in range(len(result)):
        print(result[j], end=" ")'''



x = int(input())
for i in range(x):
    y = input().split()
    if i == 0:
        a = set(y)
    else:
        a = a.intersection(set(y))
print(a)


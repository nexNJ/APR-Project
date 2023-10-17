dic = {}
num = int(input())
for x in range(num):
    fruit = input()
    if fruit not in dic:
        dic[fruit] = 1
    else:
        dic[fruit] += 1
print(dic)
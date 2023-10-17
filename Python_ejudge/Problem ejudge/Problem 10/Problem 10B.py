dic = {}
y = int(input())
for i in range(y):
    fruit = input()
    if fruit in dic:
        dic[fruit] +=1
    else:
        dic[fruit] = 1
keys = list(dic.keys())
values = list(dic.values())

keys.sort()
values.sort()


for value in values:
    for key in keys:
        if dic[key] == value:
            print(key, value)
            keys.remove(key)
            break
        
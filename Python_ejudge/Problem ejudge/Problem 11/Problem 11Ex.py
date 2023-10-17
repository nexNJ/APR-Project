dic = {}
while True:
    x = input()
    if x =="$":
        break
    (key,value) = x.split()
    value = int(value)
    if key in dic:
        dic[key] += value
    else:
        dic[key] = value
max = max(dic.values())
list = []

for key,value in dic.items():
    if value == max:
        list.append(key)
    else:
        pass
list.sort()

for h in list:
    print(h)


    
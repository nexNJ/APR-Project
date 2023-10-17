x =int(input())
list ={}
for i in range(x):
    y = input()
    if y in list.keys():
        list[y] +=1
    else:
        list[y] = 1

p = [[value,key] for key,value in list.items()]
p.sort()

for (a,b) in p:
    print(b , a)
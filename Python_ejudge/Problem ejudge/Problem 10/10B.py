x =int(input())
dic = {}
for i in range(x):
    y =input()
    if y not in dic:
        dic[y] = 1
    else:
        dic[y] +=1
print(dic)
p = [(dic[w],w) for w in dic]
p.sort()
print(p)

for value,key in p:
    print(key, value)

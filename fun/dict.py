x = {'cool': 10,'aa':5,'b':55}
x['ll'] = 50
b = x['cool']
y = sorted(x)
print(y)

for i in x:
    print(i + "|" + str(x[i]))

p = [[key,value] for key,value in x.items()]

print(p)


exit()
print(len(x))
print(sorted(x))

u = max(list(x.values()))
print(u)


k = x.get('a',5)
print(k)

exit()
print(x.keys())
print(x.values())
print(x.items())


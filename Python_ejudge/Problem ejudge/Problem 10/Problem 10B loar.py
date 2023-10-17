n = int(input())
p = {}
for i in range(n):
  y =input()
  if y not in p:
    p[y] = 1
  else:
    p[y] += 1
print(p)

a = [(p[i],i) for i in p]
a.sort()
print(a)
for (num,food) in a:
  print(food ,num)

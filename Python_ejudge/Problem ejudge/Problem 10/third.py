import math
total = int(input())
all = []

for i in range(total):
    salary = int(input())
    all.append(salary)
avg = sum(all) / total

sd = 0

print(all)
print(sum(all))
print(total)
print(avg)

for k in all:
    sd += (k - avg) ** 2
sd = round(math.sqrt(sd / total) , 2)
print(all)
for num in all:
    print(num)
    if num < (avg - sd) or num > (avg + sd):
        all.remove(num)
    else:
        continue

print(sd)
print(avg - sd, avg + sd)

print(round(sum(all) / len(all) , 2))
print(all)
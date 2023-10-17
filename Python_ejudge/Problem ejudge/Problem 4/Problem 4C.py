x = abs(int(input()))
sum = 0
list = []

while x > 0:
    if x%10 in list:
        x=x//10
        continue
    sum = sum + x%10
    list.append(x%10)
    x = x//10

print(sum)






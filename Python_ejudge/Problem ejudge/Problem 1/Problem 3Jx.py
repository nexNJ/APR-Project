y = int(input())
x = 1
sum = 0
while x < y:
    if x**2 + x > y:
        break
    elif x**2 + x <= y:
        sum += 1
        x = x+1
print(sum)

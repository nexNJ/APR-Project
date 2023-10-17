x = int(input())
result = 0

x = abs(x)
while x > 0:
    num = x % 10
    x = x//10
    result = num + result
print(result)





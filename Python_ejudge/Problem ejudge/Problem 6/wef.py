x = int(input())
result = ""
while x >0:
    y = x%2
    result = str(y) + result
    x = x//2
print(result)
    
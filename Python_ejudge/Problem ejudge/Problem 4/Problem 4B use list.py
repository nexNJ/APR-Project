x = int(input())
result = 0
for i in str(x):
    if i == "-":
        continue
    result = int(i) + result
print(result)
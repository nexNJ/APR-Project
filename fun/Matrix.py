x = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]

y = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]
result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)
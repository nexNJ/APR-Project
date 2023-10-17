upper = 120
lower = 100

for i in range(lower, upper+1):

    if i > 1:
        for num in range(i):
            if i%num == 0:
                break
            else:
                print(num)

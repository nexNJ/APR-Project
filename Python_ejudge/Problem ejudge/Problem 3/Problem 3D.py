sum = 0
while True:
    x = input()
    if x == "$":
        print(sum)
        break

    sum += int(x)

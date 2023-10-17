sum = 0
while True:
    x = input()
    if x == "$":
        print(sum)
        break
    x = int(x)
    if x < 0:
        continue

    sum += int(x)
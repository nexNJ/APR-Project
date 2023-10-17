count = 0
max = 0
min = 0

while True:
    x = input()

    if x == "$":
        if max == 0 and min == 0:
            print("Invalid input")
        else:
            print(min)
            print(max)
        break

    x = int(x)

    if count == 0:
         max = x
         min = x
    else:
        if x > max:
            max = x
        elif x < min:
            min = x
    
    count += 1

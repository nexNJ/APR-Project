s = input()
if s == "$":
    print(0)
else:
    pre = int(s)
    max_count = 1
    count = 1
    while True:
        s = input()
        if s =="$":
            break
        x = int(s)
        if x ==pre:
            count += 1
            max_count = max(max_count,count)
        else:
            pre = x
            count = 1
print(max_count)
        
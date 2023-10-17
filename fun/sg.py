

list = []
while True:
    x =input()
    if x =="$":
        break
    first,last = x.split()
    print([first,last])
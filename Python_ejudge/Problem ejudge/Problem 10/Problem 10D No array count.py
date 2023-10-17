x =input()
if x =="$":
    print(0)
else:
    max_count =1
    count = 1
    temp = int(x)
    while True:
        x = input()
        if x =="$":
            break
        if int(x) == temp:
            count+=1
        else:
            count = 1
            temp = int(x)
        max_count = max(count,max_count)
    print(max_count)
            


        
        
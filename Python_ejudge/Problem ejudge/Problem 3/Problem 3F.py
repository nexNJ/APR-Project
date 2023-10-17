x = int(input())
if x >= 1 and x < 1001:
    for i in range(1,x+1):
        if x % i  == 0:
            print(i)   
else:
    print("Invalid input")
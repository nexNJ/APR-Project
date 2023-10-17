n = int(input())
m = int(input())

if n and m > 0:
    for i in range(1,n+1):
        print(i,end=" ")
        if i % m == 0:
            print()
else:
    print("Invalid input")
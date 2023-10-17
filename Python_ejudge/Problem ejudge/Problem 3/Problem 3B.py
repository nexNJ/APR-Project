n = int(input())
m = int(input())

if n and m > 0:
    for i in range(1,m+1,1):
        for j in range(i,n+1,m):
            print(j,end=" ")
        print()
else:
    print("Invalid input")
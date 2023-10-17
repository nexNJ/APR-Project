width = int(input())
height = int(input())

for i in range(height):
    for j in range(width): 
        num = i+j
        print(num % 3,end="")
    print()
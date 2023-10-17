x = int(input())
result = ""
if x==0:
    print(0)
elif x <0 :
    print("Invalid input")
elif x > 0 or x < 2**20:
    while x > 0:
        y = x % 2 
        x = x//2
        result = str(y) + result
    print(result)

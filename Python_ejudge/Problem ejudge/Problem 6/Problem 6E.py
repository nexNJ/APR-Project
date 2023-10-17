def binary(n):
    global k
    global result
    if k == 0:
        print(0)
    elif n <=0:
        print(result)
    else:
        y = n%2
        result = str(y) + result
        binary(n//2)
x = int(input())
result = ""
k = x 
binary(x)

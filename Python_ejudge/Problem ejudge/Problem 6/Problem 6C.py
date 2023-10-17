def star(n):
    if n == 0 :
        return
    else:
        print("*"*n)
        star(n-1)

x = int(input())
star(x)
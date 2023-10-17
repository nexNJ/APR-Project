def count_up(n):
    if n ==0:
        return
    else:
        count_up(n-1)
        print(n)
x =int(input())
count_up(x)



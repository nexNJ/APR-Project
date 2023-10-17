def count_down(n):
    if n ==0:
        return
    else:
        print(n)
        count_down(n-1)
x = int(input())
count_down(x)
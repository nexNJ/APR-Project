n = int(input())
k = int(input())
list = []

if 0<= n <=1000000000 and 1<= k <=10:
    while n > 0 :
        remain = n % 16
        n = n // 16
        y = remain
        if y == 10:
            y = "A"
        elif y == 11:
            y = "B"
        elif y == 12:
            y = "C"
        elif y == 13:
            y = "D"
        elif y == 14:
            y = "E"
        elif y == 15:
            y = "F"        
        list.append(y)
    if k > len(list):
        print("0")
    else:
        print(list[k-1])

else:
    print("Invalid input")


legth = int(input())
width = int(input())

if legth and width < 0:
    print("Invalid input")
else:
    x = (legth*("*")+"\n")*width
    print(x)
    
    
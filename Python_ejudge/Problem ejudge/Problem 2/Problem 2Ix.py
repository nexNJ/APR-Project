x = int(input())
if x > 0 and x < 30 :
    if x % 2 != 0:
        y = x//2
        for i in range(0,y) :
            print(" "*i +"\\" + " "*(x-2*(i+1))+ "/")
        
        print(" "*y + 'X')

        for j in range(y,0,-1) :
            print(" "*(j-1) +"/" + " "*(x-(2*j)) + "\\")

    else :
        print("Invalid input")
else :
    print("Invalid input")
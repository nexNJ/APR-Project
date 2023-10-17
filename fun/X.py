a = int(input())

if a%2 == 0 :
    print('Invalid input')

else :

    for i in range(a) :
        for j in range(a) :
            
            if i+j == a-1 and i != (i+j)/2 : 
                print('/' , end='')

            elif i == j :

                if i == j and i == a//2  :
                    print('X' , end='')
                    
                elif i == j and i  != a//2 :
                    print('\\' , end='')

            else :
                print(' ',end='')
        print()

x = int(input())
result = ""
index_legth = len(str(x))
count = 2
digits =["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
teens = ["ten",'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ty = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

while index_legth+count > index_legth: ## 845 nine hundred and ninety nine
    if count == 2: # hundred # front to back
        if x == 0: 
            x = digits[x]
            result = x
            break
        if x < 100:
            count = count - 1           
            continue
        else:
            y = x
            x = x % 100
            y = y // 100
            y = digits[y]
            result = y + " hundred and "
            count = count - 1 


    if count == 1: ## x = 45 y= 8 
        if  x >= 20:
            y = x
            x = x % 10
            y = y // 10
            y = ty[y]
            if x == 0:
                result = result + y 
                break
            else:
                result = result + y + " " + digits[x]
                break

        elif x >= 10 :  ## 17
            x = x % 10
            x = teens[x]
            result = result + x
            break
        
        elif x != 0:
            x = x % 10
            x = digits[x]
            result = result + x
            break
        else:
            break

print(result)

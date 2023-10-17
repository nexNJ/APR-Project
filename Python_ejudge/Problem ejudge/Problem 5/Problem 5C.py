# Provide your code for function avg here
def avg(a = None,b = None,c = None):
    if a !=None and b != None and c !=None:
        x = (a+b+c)/3
    elif c == None and b != None:
        x = (a+b)/2
    elif b == None and c == None:
        x = a/1
    return round(x,2)




a = int(input())
b = int(input())
c = int(input())
print(avg(a,b,c))
print(avg(a,b))
print(avg(a))
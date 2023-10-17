# Provide your code for function progress here
def progress(d=1,num=10): # d=step num = จน output
    x = 0
    while x < num :
        result = x * d
        x = x +1
        print(result)
input()
d = input()
n = input()
input()
if (d!='') and (n!=''):
    d = int(d)
    n = int(n)
    progress(d,n)
elif (d!=''):
    d = int(d)
    progress(d)
elif (n!=''):
    n = int(n)
    progress(num=n)
else:
    progress()
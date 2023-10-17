# Provide your code for function progress here
def progress(d=1,num=10):
    for i in range(num): # 0,1234
        print(i*d)

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
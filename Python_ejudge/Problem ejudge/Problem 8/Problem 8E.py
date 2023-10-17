'''x = str(input())
list = ""
count = 0

for i in x:
    if count == 0:
        list = list + i
        count += 1
    else:
        if i in list:
            count +=1
            continue
        elif i not in list:
            if count ==1:
                print(list, end="")
                count = 1
                list = ""
                list = list + i
            else:
                print(str(count)+list,end="")
                count = 1
                list = ""
                list = list + i
if count == 1:
    print(list)       
else:
    print(str(count)+list,end="")
'''



x =input()

count = 0
list = ""
for i in x:
    if count ==0:
        pre = i
        count += 1
    else:
        if i == pre:
            count += 1
        else:

            if count ==1:
                list = list +  pre
                pre = i
            else:
                list = list + str(count) + pre
                pre = i
                count = 1
print(list+ str(count) + pre)

    
    


list1 = []

while True:
    x =input()
    if x=="$":
        break
    else:
        list1.append(int(x))
    
sortlist = list(list1) #copy list1
list1.sort(reverse = False)

if len(list1) % 2 ==0:
    med = (list1[len(list1)//2 -1]+ list1[(len(list1)//2)])/2
else:
    med = list1[len(list1)//2]
print(float(med))


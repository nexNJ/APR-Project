min=0
count = 0
while True:
    x = input()
    if x =="$":
        break
    if int(x) <0:
        continue
    if count ==0:
        min = int(x)
        count += 1
    if int(x)>0:
        if int(x) < min:
            min = int(x)
if count ==0:
    print("None")
elif min >0:
    print(min)
else:
    print("0")
list=[]
result = 0
while True:
    x =input()
    if x =="$":
        break
    else:
        list.append(int(x))

average = sum(list)/len(list)

zigma_square = 0
for i in range(0,len(list)):
    zigma_square = zigma_square+(list[i] - average)**(2)

result = (zigma_square/len(list))**(1/2)
print(round(result,2))

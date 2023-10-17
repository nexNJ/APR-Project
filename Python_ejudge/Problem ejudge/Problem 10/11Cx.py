import math
x =int(input())
list = []
sd_top = 0
for _ in range(x):
    y =int(input())
    list.append(y)

avg = sum(list)/x

for i in range(x):
    sd_top = sd_top + (list[i]-avg)**2

ans_sd = round(math.sqrt((sd_top)/x),2)

list_ans= []
for j in list:
    if j > avg+ans_sd or j < avg-ans_sd:
        pass
    else:
        list_ans.append(j)

avg_ans = round(sum(list_ans) / len(list_ans) ,2)
print(avg_ans)
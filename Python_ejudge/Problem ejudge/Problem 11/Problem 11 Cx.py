import math
num_list = []
temp_sd = 0
x = int(input())
for _ in range(x):
    y = int(input())
    num_list.append(y)

avg = round((sum(num_list) / x ),2)

for a in num_list:
    temp_sd += ((a-avg)**2)
sd = round(math.sqrt(temp_sd/x),2)

u = list(num_list)

for z in num_list:
    if z > avg+sd or z < avg-sd:
        u.remove(z)
        
#-------------------------New_Avg--------------------------#
avg = round((sum(u) / len(u) ),2)
print(avg)


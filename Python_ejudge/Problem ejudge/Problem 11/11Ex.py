dic = {}
while True:
    x =input()
    if x =="$":
        break
    [char,num] = x.split()
    num = int(num)
    if char in dic:
        dic[char] += (num)
    else:
        dic[char] = (num)
print(dic)
ans =[]
for char,num in dic.items():
    if num == max(dic.values()):
        ans.append(char)
print(ans)
ans.sort()
for i in range(len(ans)):
    print(ans[i])

    
x =input()
left = '('
right = ')'
check_left = 0
check_right = 0
count =0

if len(x) % 2 != 0:
    print("False")
else:
    for i in x:
        if i == right and check_left ==0:
            u = "False"
            break
        if i == right:
            check_right += 1
        else:
            check_left +=1
    if check_left == check_right and u != "False":
        print("True")
    else:
        if check_left != check_right or u == "False":
            print(u)


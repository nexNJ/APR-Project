def star(n,s):
    if n == 0:
        return
    else:
        print(s*" "+ n*"*")
        star(n-1,s+1)
# ****    


def count_down_stars(n,s= -1):
    if n == 1:
        return
    else:
        star(n,s+1)
        count_down_stars(n-1,s+1)
# สร้างสามเหลี่ยม


x = int(input())
count_down_stars(x)
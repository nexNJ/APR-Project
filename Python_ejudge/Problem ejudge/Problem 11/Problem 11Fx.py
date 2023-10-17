a = float(input())
b = float(input())
c = float(input())
r = 0.0
p = 0.0
r_result = 0.0
while r <= 20.0:
    p_new = (a*(r)**3) + (b*(r)**2) + (c*r)
    if p_new > p:
        p = p_new
        r_result = r
    r += 0.01
    r = round(r,2)
print(r_result)
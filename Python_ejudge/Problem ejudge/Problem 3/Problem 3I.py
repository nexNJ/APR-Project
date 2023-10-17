pricebear = int(input())
pricekitty = int(input())
money = int(input())
answer_found = False
for x in range(money // pricebear, -1, -1):
    if (money-pricebear*x)%pricekitty == 0:
        answer_found = True
        y = (money-pricebear*x) // pricekitty
        print("Teddy bear:", x, "Kitty doll:", y)
if not answer_found:
    print("Not possible")
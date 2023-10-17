price = input()
list_price = price.split()

quantity = input()
list_quantity = quantity.split()

list_price = [float(i) for i in list_price]
list_quantity = [float(i) for i in list_quantity]
total = 0
for j in range(len(list_price)):
    total += (list_price[j])*(list_quantity[j])
print(total)

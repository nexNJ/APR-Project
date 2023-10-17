x = int(input())
if x <=0 or x>20:
  print("Invalid input")
else:
  for i in range(0,x):
    print(" "*i +"*")
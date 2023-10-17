count = 0
while True:
  x = input()
  if x == "$":
    break
  if count == 0:
    num = int(x)
    max_diff = 0
    diff = 0
  else:
    diff = abs(num - int(x))
    num = int(x)
  if count ==1:
    max_diff = diff
  else:
    if max_diff < diff:
      max_diff = diff

  
  count += 1
if count < 2:
  print("Insufficient data")
else:
  print(max_diff)
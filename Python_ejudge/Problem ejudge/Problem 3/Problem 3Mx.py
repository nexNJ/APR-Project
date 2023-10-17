min = 0
max = 0
result_min =""
result_max =""
while True:
  x = str(input())
  if min == 0 and max ==0:
    min = len(x)
    max = len(x)
    result_min = x
    result_max = x
  if x == "$":
    break
  if len(x) > max:
    max = len(x)
    result_max = x
  elif len(x) < min:
    min = len(x)
    result_min = x
  else:
    pass

print(result_min)
print(result_max)

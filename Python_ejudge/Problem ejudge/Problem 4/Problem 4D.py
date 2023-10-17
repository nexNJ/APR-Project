
x = float(input())
result_front = ""
result_back = ""
decimal = float(x)-int(x)

if x > 0 and x < 2**20:
  while x > 0 :
    x = int(x)
    remain = x % 2
    x = x // 2
    result_front = str(remain) + result_front
  print(result_front+".",end="")

  ##decimal  0.2
  decimal = round(decimal,4)
  count = 0
  while count < 30:
    decimal = decimal * 2
    if decimal < 1:
      result_back = result_back + "0"
      count += 1
    elif decimal >= 1:
      result_back = result_back + "1"
      decimal = decimal - 1.0
      count += 1
  print(result_back)

elif x==0:
  print("0"+"."+"0"*30)
else:
  print("Invalid input")
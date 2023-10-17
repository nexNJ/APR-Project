x = int(input())
ball = 1

print(ball)
while True:
    ball = (ball + 3) % x
    if ball == 0:
      print(x)
    elif ball ==1:
      break
    else:
      print(ball)
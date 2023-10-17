hh = int(input())
mm = int(input())
plus = int(input())

total_minutes = hh * 60 + mm + plus
new_hh = total_minutes // 60
new_mm = total_minutes % 60
day = new_hh // 24
new_hh = new_hh % 24

if new_hh < 10:
    new_hh = "0" + str(new_hh)
if new_mm < 10:
    new_mm = "0" + str(new_mm)

print(f'{new_hh}:{new_mm}', end=" ")
if day == 1:
    print("+ 1 day")
elif day > 1:
    print(f'+ {day} days')
elif day == -1:
    print("- 1 day")
elif day < -1:
    print(f'{day} days')

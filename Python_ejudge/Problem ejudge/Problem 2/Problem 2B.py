weight = float(input())
height_cm = float(input())
height_m = 0.01 * height_cm
bmi = weight / (height_m**2)
print(round(bmi,2))
if bmi < 18.5:
    print("Below normal weight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("Class I Obesity")
elif bmi >= 35 and bmi < 40:
    print("Class II Obesity")
elif bmi >= 40:
    print("Class III Obesity")
       
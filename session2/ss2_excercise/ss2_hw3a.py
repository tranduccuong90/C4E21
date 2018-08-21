#BMI

h = float(input("Your height (cm): "))
w = float(input("Your weight (kg): "))

h_m = h/100
bmi = w/(h_m*h_m)

if bmi < 16:
    print("Severely underweigh!")
elif bmi < 18.5:
    print("Underweight!")
elif bmi < 25:
    print("Normal!")
elif bmi < 30:
    print("Overweight!")
else:
    print("Obese!")
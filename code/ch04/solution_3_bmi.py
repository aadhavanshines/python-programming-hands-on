weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / height**2
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "healthy weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"
print(f"BMI {bmi:.1f}: {category}")

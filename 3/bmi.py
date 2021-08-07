# BMI Calculator with desciption

# Accept height and weight from the user
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Calculate BMI
bmi = round(weight / height ** 2)

# Condition check with BMI
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else :
  print(f"Your BMI is {bmi}, you are clinically obese.")
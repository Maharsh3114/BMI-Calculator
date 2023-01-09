# BMI-Calculator
BODY MASS INDEX calculator using python


print("Welcome to BMI calculator")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = (weight/height**2)
bmi = round(BMI)
if bmi<=18.5:
    print(f"Your BMI is {bmi}, you are underweight.\n")

elif(bmi>18.5 and bmi<25):
        print(f"Your BMI is {bmi}, you have a normal weight.\n")

elif(bmi>25 and bmi<30):
        print(f"Your BMI is {bmi}, you are slightly overweight.\n")

elif(bmi>30 and bmi<35):
        print(f"Your BMI is {bmi}, you are obese.\n")

elif(bmi>35):
        print(f"Your BMI is {bmi}, you are clinically obese.\n")

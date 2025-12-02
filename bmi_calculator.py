# BMI Calculator Project
# Author: Anjali

def calculate_bmi(weight, height):
    """Function to calculate BMI"""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Function to decide BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

print("----- BMI CALCULATOR -----")

# Taking inputs from the user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = calculate_bmi(weight, height)

# Printing results
print("\nYour BMI is:", round(bmi, 2))
print("Category:", bmi_category(bmi))

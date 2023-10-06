#This program is used to calculate your body mass index(BMI)

height = int(input("Enter your height in inches: "))

weight = int(input("\nEnter your weight in pounds: "))

bmi = (weight * 703) / (height * height)

if bmi <= 18.5:
    classification = "underweight"
    health_risk = "minimal"

elif bmi >= 18.5 and bmi <= 24.9:
    classification = "normal weight"
    health_risk = "minimal"

elif bmi >= 25 and bmi <= 29.9:
    classification = "overweight"
    health_risk = "increased"

elif bmi >=30 and bmi <= 34.9:
    classification = "obese"
    health_risk = "high"

elif bmi >= 35 and bmi <= 39.9:
    classification = "severely obese"
    health_risk = "very high"

else:
    classification = "morbidly obese"
    health_risk = "extremely high"

print("\nYour BMI is" ,bmi, "which classifies you as", classification, "\nand your health risk is", health_risk)



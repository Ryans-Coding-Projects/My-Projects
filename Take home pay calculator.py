#This program is used to calculate take home pay

gross_income = float(input("Enter your gross income: $"))
deductions = float(input("Enter your deductions: $"))

net_income = gross_income - deductions

print(f"Your gross income: ${gross_income:.2f}")
print(f"Your deductions: ${deductions:.2f}")
print(f"Your net income (take-home pay): ${net_income:.2f}")

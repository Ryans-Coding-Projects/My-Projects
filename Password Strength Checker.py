print("-------------------------")

print("Password Strength Checker\n-------------------------")

print("0 = Extremely Weak Password\n1-3 = Very Weak Password\n4-6=Weak Password\n7-8 = Strong Password\n9 = Very Strong Password\n10=Extremely Strong Password\n-------------------------")

print("\n ")

password = input("ENTER PASSWORD HERE: ")

password_strength = 0

if any(char.isdigit() for char in password):
    password_strength += 2

if any(char.isupper() for char in password):
    password_strength += 2

if any(char.islower() for char in password):
    password_strength += 2

if len(password) >= 8:
    password_strength += 1

if any(char in "!@#$%^&*()_+-=[]{};:,.<>/?\\|" for char in password):
    password_strength += 3
    

print(" \nPASSWORD STRENGTH =" , password_strength)


lives = 3

password = input("Set Password: ")
while True:
    guess = input("Enter Password: ")

    if guess == password:
        print("Access Granted")
        break

    elif guess != password:
        lives -= 1
        print(f"Incorrect Password. {lives} attempts remaining")

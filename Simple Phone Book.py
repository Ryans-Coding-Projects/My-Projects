phone_numbers = {}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break

    if name in phone_numbers:
        print(phone_numbers[name] + " is the phone number of " + name)
    else:
        print("I do not have the phone number for " + name)
        print("What is their phone number?")
        phone = input()
        phone_numbers[name] = phone
        print("Phone number database updated.")

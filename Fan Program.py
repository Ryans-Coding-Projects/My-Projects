a = "on"
b = "off"
c = "power"
d = "option"
option = "Medium"
e = "speed"
f = "choice"
g = "power"
i=10

power = input("Fan Power - Enter [ON] or [OFF}: ").lower()

if power == "on":
    print("Fan Powered On")
    print("Fan Runnning At" , option, "Power")
    print(" ")
while i==10:
    print("-----------SETTINGS-----------")
    print("[SPEED]:Adjust Fan Speed")
    print("[POWER]: Power Fan On or Off")
    choice = input(": ").lower()
    if choice == e:
        option = input("Change Fan Speed: [LOW] [MEDIUM] [HIGH]: ").lower()
        print(" ")
        print("Fan Runnning on" , option)
    if choice == g:
        power = input("Fan Power - Enter [ON] or [OFF}: ").lower()


if power == "off":
    print("Fan Powered Off")


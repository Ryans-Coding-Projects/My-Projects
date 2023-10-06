print("This Program Will Show You The Strengths and Weaknesses For Each Pokemon Type ")

a="grass"
b="rock"
c="ice"
d="dragon"
e="dark"
f="psychic"
g="bug"
h="flying"
i="steel"
j="fire"
k="fighting"
l="ground"
m="ghost"
n="poison"
o="water"
p="fairy"
q="electric"
r="normal"

while True:

    pokemon_type = input("\nWhioh Pokemon Type Would You Like To Check?: ").lower()

    print("--------------")

    if pokemon_type=="grass":
        print("Grass Type")
        print("--------------")
        print("Strong Against : Water, Ground, Rock")
        print("Weak Against : Fire, Ice, Poison, Flying, Bug")
        print(" ")

    elif pokemon_type=="rock":
        print("Rock Type")
        print("--------------")
        print("Strong Against : Fire, Ice, Flying, Bug	")
        print("Weak Against : Water, Grass, Fighting, Ground, Steel")
        print(" ")

    elif pokemon_type=="ice":
        print("Ice Type")
        print("--------------")
        print("Strong Against : Grass, Ground, Flying, Dragon")
        print("Weak Against : Fire, Fighting, Rock, Steel")
        print(" ")

    elif pokemon_type=="dragon":
        print("Dragon Type")
        print("--------------")
        print("Strong Against : Dragon")
        print("Weak Against : Ice, Dragon, Fairy")
        print(" ")

    elif pokemon_type=="dark":
        print("Dark Type")
        print("--------------")
        print("Strong Against : Psychic, Ghost")
        print("Weak Against : Fighting, Bug, Fairy")
        print(" ")

    elif pokemon_type=="psychic":
        print("Psychic Type")
        print("--------------")
        print("Strong Against : Fighting, Poison")
        print("Weak Against : Bug, Ghost, Dark")
        print(" ")

    elif pokemon_type=="bug":
        print("Bug Type")
        print("--------------")
        print("Strong Against : Grass, Psychic, Dark")
        print("Weak Against : Fire, Flying, Rock")
        print(" ")

    elif pokemon_type=="flying":
        print("Flying Type")
        print("--------------")
        print("Strong Against : Grass, Fighting, Bug")
        print("Weak Against : Electric, Ice, Rock")
        print(" ")

    elif pokemon_type=="steel":
        print("Steel Type")
        print("--------------")
        print("Strong Against : Ice, Rock, Fairy")
        print("Weak Against : Fire, Fighting, Ground")
        print(" ")

    elif pokemon_type=="fire":
        print("Fire Type")
        print("--------------")
        print("Strong Against : Grass, Ice, Bug, Steel")
        print("Weak Against : Water, Ground, Rock")
        print(" ")

    elif pokemon_type=="fighting":
        print("Fighting Type")
        print("--------------")
        print("Strong Against : Normal, Ice, Rock, Dark, Steel")
        print("Weak Against : Flying, Psychic, Fairy")
        print(" ")

    elif pokemon_type=="ground":
        print("Ground Type")
        print("--------------")
        print("Strong Against : Fire, Electric, Poison, Rock, Steel")
        print("Weak Against : Water, Grass, Ice")
        print(" ")

    elif pokemon_type=="ghost":
        print("Ghost Type")
        print("--------------")
        print("Strong Against : Psychic, Ghost")
        print("Weak Against : Ghost, Dark")
        print(" ")

    elif pokemon_type=="poison":
        print("Poison Type")
        print("--------------")
        print("Strong Against : Grass, Fairy")
        print("Weak Against : Ground, Psychic")
        print(" ")

    elif pokemon_type=="water":
        print("Water Type")
        print("--------------")
        print("Strong Against : Fire, Ground, Rock")
        print("Weak Against : Electric, Grass")
        print(" ")

    elif pokemon_type=="fairy":
        print("Fairy Type")
        print("--------------")
        print("Strong Against : Fight, Dragon, Dark")
        print("Weak Against : Poison, Steel")
        print(" ")

    elif pokemon_type=="electric":
        print("Electric Type")
        print("--------------")
        print("Strong Against : Water, Flying")
        print("Weak Against : Ground")
        print(" ")

    elif pokemon_type=="normal":
        print("Normal Type")
        print("--------------")
        print("Strong Against : None")
        print("Weak Against : Fighting")
        print(" ")

    else:
        print("--------------")
        print("Invalid Type. Try Again")
        print("--------------")

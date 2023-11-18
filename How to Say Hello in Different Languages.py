#This program is used to say hello in 30 different languages
while True:
    hello = input("Enter a language to see how hello is said: ").capitalize()

    if hello == "English":
        print("Hello")
        break
    elif hello == "Chinese":
        print("Ní hǎo")
        break
    elif hello == "Japanese":
        print("Konnichiwa")
        break
    elif hello == "Korean":
        print("Anyeonghaseyo")
        break
    elif hello == "French":
        print("Bonjour")
        break
    elif hello == "Spanish":
        print("Hola")
        break
    elif hello == "German":
        print("Hallo")
        break
    elif hello == "Italian":
        print("Ciao")
        break
    elif hello == "Hindi":
        print("Namaste")
        break
    elif hello == "Greek":
        print("Herete")
        break
    elif hello == "Russian":
        print("Privet")
        break
    elif hello == "Portugese":
        print("Oi")
        break
    elif hello == "Arabic":
        print("Marhaba")
        break
    elif hello == "Latin":
        print("Heus")
        break
    elif hello == "Nepali":
        print("Namaste")
        break
    elif hello == "Inuktitu":
        print("Ainngai")
        break
    elif hello == "Tsalagi" or hello == "Cherokee":
        print("Osiyo")
        break
    elif hello == "Tagalog":
        print("Kamusta")
        break
    elif hello == "German":
        print("Guten Tag")
        break
    elif hello == "Irish":
        print("Haigh")
        break
    elif hello == "Latin":
        print("Salve")
        break
    else:
        print("I do not understand this language. Please try again")

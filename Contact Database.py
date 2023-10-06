names = []

phone_numbers = []

addresses = []

num = 3
print("-----------------------------------------------------------")

num = int(input("How Many Contacts Would You Like To Add?: "))

print("-----------------------------------------------------------")


for i in range(num):
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    names.append(name)
    phone_numbers.append(phone_number)
    addresses.append(address)

print("---------------------Contact Database----------------------")

print("\nName\t\t\tPhone Number\t\t\tAddress\n")


for i in range(num):
    print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], addresses[i]))

print("-----------------------------------------------------------")

search_term = input("\nEnter Search Term: ")


print("Search Contact Database: ")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    address = addresses[index]
    print("Name: {} , Phone Number: {} , Address: {}".format(search_term, phone_number, address))

else:
    print("Contact Not Found")


    



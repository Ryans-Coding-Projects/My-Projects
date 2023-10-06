#This program generates a random password.

#Import random
import random

#Define and set values for random password.
def random_password(length, chars=None):
    if chars == None:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+/*\\|<>;:"

    password = ""
    for i in range(length):
        password += random.choice(chars)

    return password

#Display results
print(random_password(16))





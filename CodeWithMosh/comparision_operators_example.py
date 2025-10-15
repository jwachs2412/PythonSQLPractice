temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Enjoy your day")


# If name has less than 3 characters, it's too short
# Name must be at least 3 characters
# Otherwise, if name has more than 50 characters, it's too long
# Name can be a maximum of 50 characters
# Otherwise
# Name looks good

name = len(input("Please enter your name: "))
if name < 3:
    print("Name must be at least 3 characters")
elif name > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")

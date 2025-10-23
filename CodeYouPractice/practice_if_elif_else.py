age = int(input("Please enter your age: "))

if age >= 100:
    print("You're too old to sign up.")
elif age >= 18 and age < 100:
    print("You're now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You're not eligible. You must be 18+ to sign up.")


response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")


name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!!")
else:
    print(f"Hello {name}")


for_sale = True

if for_sale:
    print("This is item is for sale.")
else:
    print("This item is not for sale.")

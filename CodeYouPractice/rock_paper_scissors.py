import random

listOfChoices = ['rock', 'paper', 'scissors']

while True:
    userChoice = input(
        "Please select 'Rock', 'Paper', or 'Scissors': ").lower()

    if userChoice in listOfChoices:
        print("The game will proceed.")
        break
    else:
        print("Your entry isn't in the list of choices. You need to choose 'Rock', 'Paper' or 'Scissors'.")
        continue

cpuChoice = random.choice(listOfChoices)

print(
    f"You chose: {userChoice.upper()} and the computer chose: {cpuChoice.upper()}")

if userChoice == cpuChoice:
    print("It's a tie!")
elif ((userChoice == 'rock' and cpuChoice == 'scissors') or (userChoice == 'scissors' and cpuChoice == 'paper') or (userChoice == 'paper' and cpuChoice == 'rock')):
    print("Congrats! You beat the computer!")
else:
    print("Hahaha! You lost to a computer!")

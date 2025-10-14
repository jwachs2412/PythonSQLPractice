# Generate a random number
# Ask the user to make a guess
# If not a valid number
#   Print an error message
# If number < guess
#   Print "Too low"
# If number > guess
#   Print "Too high"
# Else
#   Print "You guessed it"


# Mosh's solution
"""
import random 

number_to_guess = random.randint(1, 100)

while True:
  try:
    guess = int(input('Guess the number between 1 and 100: '))

    if guess < number_to_guess:
      print('Too low!')
    elif guess > number_to_guess:
      print('Too high!')
    else:
      print('Congratulations! You guessed the number.')
      break
  except ValueError:
    print('Please enter a valid number')
    
"""


import random


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


min_num = get_int("Enter the minimum number for the guessing range: ")
max_num = get_int("Enter the maximum number for the guessing range: ")
number_to_guess = random.randint(min_num, max_num)
guesses_taken = 1

while True:
    try:
        guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
        if guess < number_to_guess:
            print("Too low! Try again.")
            guesses_taken += 1
        elif guess > number_to_guess:
            print("Too high! Try again.")
            guesses_taken += 1
        elif guesses_taken == 10:
            print("Sorry, you've used all your attempts. The number was",
                  number_to_guess)
            break
        else:
            print("You guessed it! The number was", number_to_guess)
            print("You guessed the number in", guesses_taken, "attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")

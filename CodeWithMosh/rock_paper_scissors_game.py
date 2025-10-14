# Ask the user to make a choice
# If choice is not valid
#   Print an error message
# Let the computer to make a choice
# Print choices (emojis)
# Determine the winner
# Ask the user if they want to play again
# If not
#   Terminate the program

# Mosh's solution
"""
import random

ROCK = 'r' # uppercase letters for constants
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def get_user_choice():
  while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice in choices:
      return user_choice      
    else:
      print('Invalid choice!')
      
def display_choices(user_choice, computer_choice):
  print(f'You chose {emojis[user_choice]}')
  print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print('Tie!')
  elif (
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == SCISSORS and computer_choice == PAPER) or 
    (user_choice == PAPER and computer_choice == ROCK)):
    print('You win')
  else:
    print('You lose')  

def play_game():
  while True:
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)

    display_choices(user_choice, computer_choice)

    determine_winner(user_choice, computer_choice)

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
      break

play_game()

"""

import random

while True:
    player_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    computer_choice = random.choice(['r', 'p', 's'])

    if player_choice == 'r':
        print("You chose 🪨")
    elif player_choice == 'p':
        print("You chose 📄")
    elif player_choice == 's':
        print("You chose ✂️")
    else:
        print("Invalid choice! Please choose 'r', 'p', or 's'.")
        continue

    if computer_choice == 'r':
        print("Computer chose 🪨")
    elif computer_choice == 'p':
        print("Computer chose 📄")
    elif computer_choice == 's':
        print("Computer chose ✂️")

    if ((player_choice == 'r' and computer_choice == 's') or
        (player_choice == 'p' and computer_choice == 'r') or
            (player_choice == 's' and computer_choice == 'p')):
        print("You win!")
    elif player_choice == computer_choice:
        print("It's a tie!")
    else:
        print("Computer wins!")
    keep_playing = input("Play again? (y/n): ").lower()
    if keep_playing != 'y':
        print("Thanks for playing!")
        break

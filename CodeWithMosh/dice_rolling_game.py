# Loop
# Ask: roll the dice?
# If user enters y
#   Generate 2 random numbers
#   Print the numbers
# If user enters n
#   Print thank you message
#   Terminate
# Else
#   Print invalid choice

# Mosh's solution
"""
import random 

while True:
  choice = input('Roll the dice? (y/n): ').lower()
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')
"""


import random
roll = "y"
num_list = []

while roll == "y":
    num_list.clear()
    num_dice_to_roll = (input("How many dice do you want to roll? "))
    for _ in range(int(num_dice_to_roll)):
        num_rolled = random.randint(1, 6)
        num_list.append(num_rolled)
    print(num_list)

    roll = input("Roll the dice? (y/n): ").lower()
    if roll != "y":
        print("Thanks for playing!")
        break

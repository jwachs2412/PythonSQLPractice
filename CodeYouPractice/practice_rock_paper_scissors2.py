"""
    By splitting these into three separate functions, we maintain the same efficiency while making the code much easier to follow. This also improves flexibility. If we ever want to modify the rules, add new choices, or expand the game, making changes will be much simpler and more manageable.

    Returns:
        _type_: _description_
"""

import random as rand


def get_computer_choice() -> str:
    """Returns a random choice of 'rock', 'paper', or 'scissors'."""
    choices: list[str] = ["rock", "paper", "scissors"]
    return rand.choice(choices)


def determine_winner(user_choice: str, computer_choice: str) -> str:
    """Determines the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return f"Both chose {user_choice}. It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return f"You chose {user_choice}, computer chose {computer_choice}. You win!"
    else:
        return f"You chose {user_choice}, computer chose {computer_choice}. You lose!"


def rps(user_choice: str) -> str:
    """Handles the Rock-Paper-Scissors game flow."""
    user_choice = user_choice.lower()  # Normalize input
    if user_choice not in ["rock", "paper", "scissors"]:
        return "Invalid choice! Please choose rock, paper, or scissors."

    computer_choice: str = get_computer_choice()
    return determine_winner(user_choice, computer_choice)


# Example usage
print(rps("rock"))

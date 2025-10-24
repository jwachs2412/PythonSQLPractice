# Define the dictionary with books and their availability
library = {
    "The Hobbit": "Available",
    "Slaughterhouse-Five": "Available",
    "Moby Dick": "Available",
    "The Catcher in the Rye": "Checked Out",
    "Siddhartha": "Checked Out",
    "Meditations": "Checked Out",
    "Things Fall Apart": "Available",
    "To Kill a Mockingbird": "Checked Out",
    "Pride and Prejudice": "Available",
    "Jane Eyre": "Checked Out",
    "The Great Gatsby": "Available",
    "War and Peace": "Checked Out",
    "Crime and Punishment": "Available",
    "Brave New World": "Available",
    "A Tale of Two Cities": "Checked Out",
    "Animal Farm": "Available",
    "Dracula": "Checked Out",
    "Frankenstein": "Available",
    "The Road": "Available",
    "The Alchemist": "Checked Out"
}

# Finding and printing books that start with 'T'
# print("Books that start with 'T':")
# for book in library.keys():
#     if book.startswith("T"):
#         print(book)

# Ask the user for a letter to search for.
# Use .upper() and .strip() so it works even if they enter lowercase or spaces.
# Example: If the user types " t ", it should become "T".
letter = input("Please enter a letter to search for: ").upper().strip()
print(letter)

# Create a variable to keep track of how many books match the search.
numBooks = 0

# Print a friendly message before listing the results. (Just run this cell, no need to make changes)
print(f"\nBooks starting with {letter} that are Available:")

# Loop through the book dictionary to check each title.
# Example: for title, status in library.items():
# If the title starts with the chosen letter and the status is "Available",
# print the title and increase match_count by 1.
for title, status in library.items():
    if title.startswith(letter) and status == "Available":
        print(title)
        numBooks += 1

# After the loop, print how many books matched.
print(f"\nNumber of matching available books: {numBooks}")
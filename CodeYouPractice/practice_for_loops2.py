library = {
    "The Great Gatsby": "Available",
    "1984": "Checked Out",
    "To Kill a Mockingbird": "Available",
    "Pride and Prejudice": "Available",
    "The Catcher in the Rye": "Checked Out",
    "The Hobbit": "Available",
}

print("Books that start with 'T': ")
for book in library.keys():
    if book.startswith("T"):
        print(book)

# Prints 1 2 3 on a line three times
for x in range(3):
    for y in range(1, 4):
        print(y, end=" ")
    print()

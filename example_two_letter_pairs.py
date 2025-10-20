import string

lowercase_alphabet = string.ascii_lowercase

# Print all possible two-letter combinations
for first_letter in lowercase_alphabet:
    for second_letter in lowercase_alphabet:
        print(first_letter + second_letter)

# Now print only pairs where the letters are different
for first_letter in lowercase_alphabet:
    for second_letter in lowercase_alphabet:
        if first_letter != second_letter:
            print(first_letter + second_letter)

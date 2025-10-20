import string

lowercase_alphabet = string.ascii_lowercase

for first_letter in lowercase_alphabet:
    for second_letter in lowercase_alphabet:
        print(first_letter + second_letter)
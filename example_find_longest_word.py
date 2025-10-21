import string


def longest_word(input_text):
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    clean_text = input_text.translate(translator)

    words = clean_text.split()
    max_word = ""
    max_length = 0

    for word in words:
        clean_word = word.strip(string.punctuation)
        if len(clean_word) > max_length:
            max_length = len(clean_word)
            max_word = clean_word

    return max_word


print(longest_word("The quick brown fox jumps over the lazy dog"))  # Output: "jumps"
# Output: "thousand"
print(longest_word("A journey of a thousand miles begins with a single step"))
# Output: "question"
print(longest_word("To be or not to be, that is the question"))
print(longest_word("All that glitters is not gold"))  # Output: "glitters"

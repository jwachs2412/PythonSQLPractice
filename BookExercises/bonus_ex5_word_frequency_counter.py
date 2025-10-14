from collections import Counter
import string

def word_frequency():
    with open("text.txt", "r") as file:
        text = file.read().lower().translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        counter = Counter(words)
        
    print("Top 5 most frequent words:")
    for word, count in counter.most_common(5):
        print(f"{word}: {count}")
        
word_frequency()
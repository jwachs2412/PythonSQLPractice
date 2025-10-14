file_name = "sample.txt"
word_count = {}

with open(file_name, "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower().strip(".,!?")
            word_count[word] = word_count.get(word, 0) + 1
            
for word, count in word_count.items():
    print(f"{word}: {count}")
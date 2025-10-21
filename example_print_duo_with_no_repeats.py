FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

new_flavors_list = []

for x in FLAVORS:
    for y in FLAVORS:
        if x != y:
            normalized_pair = tuple(sorted((x, y)))
            if normalized_pair not in new_flavors_list:
                new_flavors_list.append((normalized_pair))
                print(x, y, sep=", ")

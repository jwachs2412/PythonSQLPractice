x = {"name": "Josh",
     "age": 51
     }
# name = key
# Alice = value
# Key and value together form a key-value pair
print(x["name"])

# Nested dictionary
y = {
    "name": "Josh",
    "age": 51,
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
print(y["address"]["city"])  # Output: New York

# Nested dictionary with more depth
z = {
    "Sajjad": {"math": 90, "science": 85},
    "David": {"math": 95, "science": 80}
}

z["Sajjad"]["math"] = 100  # Update Sajjad's math score

print(z["Sajjad"]["math"])  # Output: 90

print(z)  # Print the entire dictionary

z["Alex"] = {"math": 88, "science": 92}  # Add a new student

print(z)  # Print the updated dictionary

a = {
    "Sajjad": {"math": 90, "science": 85},
    (1, 2): "tuple as a key",  # tuple as a key
    42: "integer as a key",  # integer as a key
    "x": [1, 2, 3],  # list as a value
    "y": (4, 5, 6),  # tuple as a value
}

print(a.keys())    # Print all keys dict_keys
print(a.values())  # Print all values dict_values
print(a.items())   # Print all key-value pairs

my_copy = dict = a.copy()  # Create a shallow copy of the dictionary
print(my_copy)  # Print the copied dictionary

# Show that the original and copied dictionaries are different objects; updates to one will affect the other only if the values are mutable and modified in place
# To avoid this, use deepcopy from the copy module for nested dictionaries
print(id(a))        # Print the memory address of the original dictionary
print(id(my_copy))  # Print the memory address of the copied dictionary

print(a.get("Sajjad"))  # Safely get value for key "Sajjad"

# Safely get value for non-existent key with default
print(a.get(999, "Not Found"))

print(a.setdefault("Sajjad", "???"))  # Returns existing value for "Sajjad"
print(a.setdefault(999, "???"))  # Adds key 999 with value "???"
print(a)  # Print the dictionary after setdefault

popped: str = a.pop(42)       # Remove the key-value pair with key 42
print(popped)    # Print the popped value
del a[42]          # Another way to remove key 42
print(a)         # Print the dictionary after popping key 42

a.popitem()  # Will remove the last inserted item in Python 3.7+
print(a)         # Print the dictionary after popping an item

a.clear()        # Clear the dictionary
print(a)         # Output: {}

people: list[str] = ["Josh", "David", "Alex"]  # List of people

# Create a dictionary with default value
users: dict = dict.fromkeys(people, "unknown")

# Output: {'Sajjad': 'unknown', 'David': 'unknown', 'Alex': 'unknown'}
print(users)

print(users.items())  # Print all key-value pairs

for k, v in users.items():
    print(f'Key: {k}, Value: {v}')

workers: dict = {0: "Josh", 1: "David", 2: "Alex"}
# Update the dictionary with new key-value pairs, existing key 2 will be updated
workers.update({2: "Sajjad", 3: "Mosh"})

print(workers)  # Output: {0: 'Josh', 1: 'David', 2: 'Sajjad', 3: 'Mosh'}

# Merges two dictionaries, requires Python 3.9+, | is the same as update() but returns a new dictionary
print(workers | {10: "New Worker", 11: "Harry"})
print(workers)  # Original dictionary remains unchanged
workers |= {12: "Another Worker"}  # In-place merge, same as update()
print(workers)  # updates the original dictionary

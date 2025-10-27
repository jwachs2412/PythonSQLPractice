customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"

print(customer["name"])
print(customer.get("name"))
# print(customer["birthdate"]) # Throws KeyError because birthdate doesn't exist as a key
# returns None because get method will give you absence of value rather than error
print(customer.get("birthdate"))
print(customer)


phone = input("Phone: ")
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# Example 1 - For
for number in range(1, 10, 2):
    print("Attempt", number, number * '.')


# Example 2 - For..Else
successful = True

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

successful2 = False

for number in range(3):
    print("Attempt")
    if successful2:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# Example 3 - Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# Example 4 - Iterables
for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)


# Practice (uses more memory because we are storing numbers in a list and then getting the count in our print statement)
evenNumList = []

for x in range(1, 10):
    if x % 2 == 0:
        evenNumList.append(x)
        print(x)
print(f"We have {len(evenNumList)} even numbers")

# Practice - Mosh's solution (uses less memory; just doesn't store the numbers which we don't technically need to in the example)
count = 0

for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers.")

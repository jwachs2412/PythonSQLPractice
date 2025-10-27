for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


numbers = [5, 2, 5, 2, 2]

for x in numbers:
    for y in range(x):  # We could do print("x" * x) but for practicing nested loops we don't want to do that
        print("x", end="")
    print()

# Another way to solve
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)

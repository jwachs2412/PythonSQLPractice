endingNum = int(input("Please enter a number to stop at: "))

for x in range(1, endingNum + 1):
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

import math  # imports math module

name = input('What is your name? ')
print(f'Hello {name}')
color = input('What is your favorite color? ').lower()
print(f'{color} is a nice color')
print(f'{name} likes {color}')
birth_year = input('What year were you born? ')
print(type(birth_year))
age = 2025 - int(birth_year)
print(type(age))
print(f'You are {age} years old')
weight_lbs = input('What is your weight in pounds? ')
print(type(weight_lbs))
weight_kg = int(weight_lbs) * 0.454
print(f'You are {weight_kg} kg which is {weight_lbs} pounds')

course = 'Python for Beginners'
print(course.upper())  # converts to uppercase
print(course.lower())  # converts to lowercase
print(course.find('P'))  # returns index of first occurrence of substring
print(course.replace('Beginners', 'Absolute Beginners'))  # replaces substring
# checks if substring exists in string, returns boolean
print('Python' in course)
print('python' in course)  # case-sensitive, returns false
print(len(course))  # returns length of string

print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 / 3)  # division always results in a float
print(10 // 3)  # floor division removes decimal
print(10 % 3)  # modulus operator gives remainder
print(10 ** 3)  # exponentiation operator

x = 10
x += 3  # x = x + 3
print(x)
x -= 3  # x = x - 3
print(x)
x *= 3  # x = x * 3
print(x)
x /= 3  # x = x / 3
print(x)
x //= 3  # x = x // 3
print(x)
x %= 3  # x = x % 3
print(x)
x **= 3  # x = x ** 3
print(x)

x = 2.9
print(round(x))  # rounds to nearest integer
print(abs(-2.9))  # returns absolute value
math.ceil(x)  # rounds up to nearest integer
math.floor(x)  # rounds down to nearest integer
math.sqrt(36)  # returns square root

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day\nDrink plenty of water")
elif is_cold:
    print("It's a cold day\nWear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

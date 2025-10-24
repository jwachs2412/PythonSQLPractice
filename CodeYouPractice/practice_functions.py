def first_func():
    print("Hello World!")


first_func()


def num_squared(num):
    print(num**2)


num_squared(3)
num_squared(83)
num_squared(33)


def num_squared_cust(num, power):
    print(num**power)


num_squared_cust(5, 3)
num_squared_cust(10, 4)

# Arbitrary Args *
args_tuple = (5, 6, 1, 2, 8)


def num_args(*number):
    print(number[0]*number[1])


num_args(*args_tuple)

# Keyword Argument


def num_kwarg(**number):
    print('My number is: ' + number['integer'] +
          '. My other number: ' + number['integer2'])


num_kwarg(integer='2309', integer2='349')


# Docstrings
def add(a: int, b: int) -> int:
    """ returns the sum of the two integers"""
    return a + b


print(add, __doc__)

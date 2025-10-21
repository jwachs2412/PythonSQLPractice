first_num = int(input("Enter a starting number for your range: "))
second_num = int(input("Enter an ending number for your range: "))


def divisible_by(starting_num, ending_num):
    for x in range(starting_num, ending_num + 1):
        if x % 7 == 0:
            n = sum(int(x) for x in str(x))
            if n % 3 == 0:
                print(x)


divisible_by(first_num, second_num)

first_num2 = 0
second_num2 = 1000


def divisible_by2(starting_num2, ending_num2):
    for x in range(starting_num2, ending_num2 + 1):
        if x % 7 == 0:
            n = sum(int(x) for x in str(x))
            if n % 3 == 0:
                print(x)


divisible_by(first_num2, second_num2)

def print_even_numbers(start, stop):
    for x in range(start, stop):
        if x % 2 == 0:
            print(x)


# Example usage
print_even_numbers(1, 10)  # Output: 2, 4, 6, 8
print_even_numbers(5, 15)  # Output: 6, 8, 10, 12, 14
print_even_numbers(0, 5)   # Output: 0, 2, 4
print_even_numbers(-5, 5)  # Output: -4, -2, 0, 2, 4
print_even_numbers(10, 20)  # Output: 10, 12, 14, 16, 18
print_even_numbers(3, 3)   # Output: (no output)
print_even_numbers(-10, -1)  # Output: -10, -8, -6, -4, -2

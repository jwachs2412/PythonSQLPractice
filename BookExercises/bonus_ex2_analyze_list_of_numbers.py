def analyze_numbers():
    numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    
    if not numbers:
        print("You submitted an empty list. Not cool! Please try again.")
        return analyze_numbers()
    else:
        print(f"Sum: {sum(numbers)}")
        print(f"Average: {sum(numbers) / len(numbers)}")
        print(f"Max: {max(numbers)}, Min: {min(numbers)}")
        print("Even numbers:", [num for num in numbers if num % 2 == 0])
        print("Sorted list:", sorted(numbers))
    
analyze_numbers()
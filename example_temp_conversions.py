def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    print(f"{temp} degrees fahrenheit is equal to {celsius} degrees celsius.")


def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9 / 5 + 32)
    print(f"{temp} degrees celsius is equal to {fahrenheit} degrees fahrenheit.")


# Example usage
fahrenheit_to_celsius(32)  # Output: 0.0
fahrenheit_to_celsius(100)  # Output: 37.77777777777778
celsius_to_fahrenheit(0)    # Output: 32.0
celsius_to_fahrenheit(37.5)  # Output: 99.5

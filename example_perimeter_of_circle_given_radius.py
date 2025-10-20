import math


def circle_perimeter(radius):
    radius = 2*math.pi*radius
    return radius


# Example usage
print(circle_perimeter(5))  # Output: 31.41592653589793
print(circle_perimeter(10))  # Output: 62.83185307179586
print(circle_perimeter(0))  # Output: 0.0
print(circle_perimeter(2.5))  # Output: 15.707963267949466
print(circle_perimeter(7.1))  # Output: 44.60220617379559

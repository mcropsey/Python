import math
from typing import List, Iterator

# Basic syntax, data types, and list comprehensions
def square_even_numbers(numbers: List[int]) -> List[int]:
    """Return a list of squares for each even number."""
    return [x ** 2 for x in numbers if x % 2 == 0]

# Functions, error handling, and lambda functions
def safe_divide(a: float, b: float) -> float:
    """Divides a by b, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return float('inf')  # Return infinity to indicate error

# Object-oriented programming (OOP) and classes
class Circle:
    """A class representing a circle."""

    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self) -> float:
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius

# Decorators
def debug(func):
    """A decorator to print function call details for debugging."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

# Generators and iterators
def fibonacci(n: int) -> Iterator[int]:
    """Generate the first n numbers in the Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Context managers and file handling
def read_file(file_path: str) -> str:
    """Read a file using a context manager."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

# Main execution to demonstrate all functions and concepts
if __name__ == "__main__":
    # Basic syntax, list comprehensions, and data types
    numbers = [1, 2, 3, 4, 5, 6]
    print("Squared even numbers:", square_even_numbers(numbers))

    # Error handling and lambda functions
    print("Safe divide:", safe_divide(10, 0))

    # OOP with classes
    circle = Circle(radius=5)
    print("Circle area:", circle.area)
    print("Circle circumference:", circle.circumference)

    # Decorator usage
    print("Addition with debug:", add(5, 7))

    # Generators
    print("Fibonacci sequence:", list(fibonacci(10)))

    # Context manager and file handling
    print("File content:", read_file("example.txt"))

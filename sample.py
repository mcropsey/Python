

# 1. Using help() to get information about a built-in function
print("Using help() to learn about a function:\n")
help(print)  # Shows the documentation for the `print` function

# 2. Using print() to display messages or results
print("\nUsing print() to display text and results:")
print("Hello, world!")

# 3. Using enumerate() to get index-value pairs from an iterable
print("\nUsing enumerate() to get index-value pairs:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit {index}: {fruit}")

# 4. Using range() to generate a sequence of numbers
print("\nUsing range() to generate a sequence of numbers:")
for number in range(1, 6):  # Generates numbers from 1 to 5
    print(number)

# 5. Using zip() to combine multiple iterables element-wise
print("\nUsing zip() to combine lists element-wise:")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# 6. Using filter() to filter elements based on a condition
print("\nUsing filter() to filter even numbers from a list:")
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 7. Using map() to apply a function to each element in a list
print("\nUsing map() to square each number in a list:")
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)


# A simple Python program to demonstrate basic concepts for a job interview

# Function to reverse a string
def reverse_string(input_string):
    """
    This function takes a string as input and returns the reversed string.
    """
    return input_string[::-1]

# Function to count the occurrences of each character in a string
def count_characters(input_string):
    """
    This function takes a string as input and returns a dictionary with
    the count of each character in the string.
    """
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Class to represent a simple bank account
class BankAccount:
    """
    A simple class to represent a bank account with basic operations.
    """
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.
        """
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        """
        Returns a string representation of the bank account.
        """
        return f"BankAccount(owner={self.owner}, balance=${self.balance})"

# Main function to demonstrate the use of the above functions and class
def main():
    # Example of string operations
    example_string = "hello world"
    print(f"Original string: {example_string}")
    reversed_string = reverse_string(example_string)
    print(f"Reversed string: {reversed_string}")

    # Example of counting characters in a string
    char_count = count_characters(example_string)
    print(f"Character counts: {char_count}")

    # Example of using a list with a for loop
    numbers = [1, 2, 3, 4, 5]
    print("Numbers in the list:")
    for number in numbers:
        print(number, end=" ")
    print()

    # Example of using a while loop to find the sum of numbers in a list
    total = 0
    index = 0
    while index < len(numbers):
        total += numbers[index]
        index += 1
    print(f"Sum of numbers: {total}")

    # Example of using if/then statements
    if total > 10:
        print("The sum is greater than 10.")
    else:
        print("The sum is 10 or less.")

    # Example of using a dictionary
    student_grades = {"Alice": 90, "Bob": 85, "Charlie": 95}
    print("Student grades:")
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")

    # Example of using the BankAccount class
    account = BankAccount("John Doe", 100)
    print(account)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200)  # This should show insufficient funds

# Run the main function
if __name__ == "__main__":
    main()
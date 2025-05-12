name = input("Please enter first name:  ")
print(f"\nHello, {name}!\n\n")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your last name?  "

name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you?  ")
age = int(age)

if age >= 21:
	print("You are 21 or older.")
else:
	print("You are under age 21.")


def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!\n")

prompt = "Enter your username:  "
user = input(prompt)

greet_user(user)

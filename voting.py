age = 17

if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

age = 1
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("You admission cost is $40.")

age = 12


if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"You admission cost is ${price}.")



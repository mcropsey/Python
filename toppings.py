requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

# check to ensure list isn't empty this time

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
else:
	print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineaple', 'extra_cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
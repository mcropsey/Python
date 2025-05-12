def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)

def make_pizza2(*toppings):
	"""Summarize the pizza we are about to make"""
	print("\nMaking a pizza with the folling toppings:")
	for topping in toppings:
		print(f" - {topping}")

def make_pizza3(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMake a {size}-inch pizza with the fowllowing toppings:")
	for topping in toppings:
		print(f"- {toppings}")


# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following topings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")

print("Another way to print the dictionary list:")
print(pizza['toppings'])

print("\n\nUsing a function with arbitary number of arguments")
make_pizza('pepperoni')
make_pizza('Mushrooms', 'green peppers', 'extra cheese')


print("\n\nArbitary number of arguments but with for loop in fucntion")
make_pizza2('pepperoni')
make_pizza2('Mushrooms', 'green peppers', 'extra cheese')

print ("\n\nNow we mix positional and arbitary set of arguments")
make_pizza3(16, 'pepperoni')
make_pizza3(12, 'mushrooms', 'greeen peppers', 'extra cheese')


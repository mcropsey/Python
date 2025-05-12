def describe_pet(animal_type, pet_name='Mac'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Way to not have to worry about order of passing arguments
# bad results
describe_pet('willie', 'dog')
# correct results no matter the order passed
describe_pet(pet_name='willie', animal_type='dog')
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(animal_type='dog')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"This is the oringal list:  {cars}.")
cars.reverse()
print(f"Reverse order list:  {cars}.")
print(f"Reverse permenant or not?  {cars}.")
print("I guess it was.")

motorcycles = ['Harley-Davidson', 'Indian', 'Ducati', 'Triumph']
print(motorcycles)
print(f"The number of motorcycles is {len(motorcycles)}.")
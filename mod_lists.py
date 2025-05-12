motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
print("\n\n\n\n\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("\n\n\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I woned was a {last_owned.title()}.")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first owned was a {first_owned.title()}.")
print (motorcycles)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Lowest number in list: {min(digits)}")
print(f"Highest number in list: {max(digits)}")
print(f"Sum of all digits in list: {sum(digits)}")




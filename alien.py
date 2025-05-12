alien_0 = {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}

print(alien_0['color'])
print(alien_0['points'])

print (alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['pints'] = 5
print (f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position:  {alien_0['x_position']}")

# Move alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position:  {alien_0['x_position']}")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


alien_0 = {'color': 'green', 'speed': 'slow'}
# below will return a key error their is no points key
# print(alien_0['points'])

#use get with a default value to fix above
print_value = alien_0.get('points', 'No point value assigned.')
print(print_value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
	pass

print("\n\n")

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens. NOTE:  Array :5 is begining to 5th item
for alien in aliens[:5]:
	print(alien)

print("...")

# Show how many aliens have been created.
print(f"Total number of aliens:  {len(aliens)}")

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")






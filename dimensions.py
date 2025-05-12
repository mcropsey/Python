dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# if you uncomment below you will get a compliler error
#dimensions[0] = 250

# Tuples defined by comma, parentheses just for neatness
# If you want only one item you still need the comma
my_t = (3,)

print("\n\n")

for dimension in dimensions:
    print(dimension)

# You can't modify a Tuple but you can assign a new value

print("\n\n")
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
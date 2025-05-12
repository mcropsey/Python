my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods[0] = "NONE"
print(f"my_foods\t\t:\t\t  {my_foods}")
print(f"friend_foods\t:\t\t  {friend_foods}")
print("\nNOTE:  As you can see when you are not making a copy but simply using = operator.\n")


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods[0] = "NONE"
print(f"my_foods\t\t:\t\t  {my_foods}")
print(f"friend_foods\t:\t\t  {friend_foods}")
print("\nNOTE:  Using [:] operator a copy is made so when I mode friends list original is preserved.\n")
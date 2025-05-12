answer = 19

if answer != 42:
	print("That is not the correct answer.  Please try again!")

if answer < 42:
	print("Answer is less than 42")

if answer > 17:
	print("Answer is more than 17")


age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 <= 18:
	print("Both conditions satisfied")

if age_0 > 22 or age_1 <19:
	print("Something passed.")

requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in requested_toppings:
	print("We want mushrooms")

banned_users = ['andrew', 'carolina', 'david']

user='marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")




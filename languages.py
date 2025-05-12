favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}

print(f"Sarah's favorite_languages are:   {favorite_languages['sarah']}")

print(f"Entire dictionary is:  {favorite_languages}")



print ("\n\n\n\n")

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
	print(name.title())


#Same Result as keys is default
print("\n\n")

for name in favorite_languages:
	print(name.title())

print("\n\n\n\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"hi {name.title()}.")
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\n{name.title()}, I see you love {language}!")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}

print("\n\n")
if 'erin' not in favorite_languages.keys():
	print("Erin, please take out poll!")

favorite_languages = {
	'jen': 'python',
	'sara': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("\n\nSorted Version:\n")
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")
print("\n\n")


favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
print("\n\nList without repeats:")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
print("\n\n")

# Using a set verses a dictionary, still use the braces
languages = {'python', 'ruby', 'python', 'c'}
print(languages)

favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

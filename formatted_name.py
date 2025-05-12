def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formated."""
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

def build_person(first_name, last_name, age=None):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = get_formatted_name('jimi', 'hendrix', 'hooker')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = build_person('Michael', 'Jackson')
print(musician)

musician = build_person('jimi', 'hendrix', 16)
print(musician)

#alien.py
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color':'green', 'points':5}

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")


#Adding New key-value pairs
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['X position'] = 0
# alien_0['Y position'] = 25
# print(alien_0)

#starting with an empty Dictionary
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

#Modifying values in a dictionary
# alien_0 = {'color':'green', 'points':5}
# print(
# f"The alien color is {alien_0['color']},\nSo you earn {alien_0['points']}")

# alien_0['color'] = 'yellow'
# alien_0['points'] = 10

# print(
# f"The alien color is {alien_0['color']},\nSo you earn {alien_0['points']}")


# alien_0 = {'color':'green', 'points':5, 'X_position':0, 'Y_position':25, 
# 'speed':'medium'}
# print(f"The original position: {alien_0['X_position']}")

# #Move the alien to the right 
# determine how far to move the alien based on its current speed
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['X_position'] = alien_0['X_position'] + x_increment


# print(f"New position: {alien_0['X_position']}")


#Removing Key-value pair
# alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

#A Dicitionary of similar objects 
#favorite.py
# favorite_languages = {
#     'jen': 'pythons',
#     'sarah': 'C',
#     'edward': 'rust',
#     'phil': 'python'
# } 

# language = favorite_languages['sarah'].title()
# print(f"Sarah's Favorite language is {language}")


#6-1 person
# first_name = input('Enter your first name:')
# last_name = input('Enter your second name:')
# age = int(input("Enter your age:"))
# city = input("Enter your location currently:")

# person = {
#     'first-name' : first_name,
#     'last-name' : last_name,
#     'age' : age,
#     'location' : city
# }
# print("\nbelow is the data in this dictionary:")
# print(f"Name:{person['first-name']} {person['last-name']}")
# print(f"Age:{person['age']}")
# print(f"Location:{person['location']}")

#6-2 
#favorite number 
# favorite_number = {
#     'john': 5,
#     'stacey':20,
#     'lee':4,
#     'arron':54,
#     'terry':64
# }
# print(f"John's favorite number is {favorite_number['john']}")
# print(f"Arron's favorite number is {favorite_number['arron']}")
# print(f"Lee's favorite number is {favorite_number['lee']}")
# print(f"Terry's favorite number is {favorite_number['terry']}")
# print(f"Stacey's favorite number is {favorite_number['stacey']}")



#looping through a dictionary
#user.py
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f"\nkey: {key}")
#     print(f"value: {value}")

# favorite_language = {
#     'jen': 'python',
#     'sarah':'c',
#     'edward':'rust',
#     'phil':'python'

# }

# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")


#Looping through all keys in a dictionary
# favorite_language = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'rust',
#     'phil': 'python'
# }

# for name in favorite_language.keys():
#     print(name.title())


#continue code


# favorite_language = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'rust',
#     'phil': 'python'
# }

# friends = {'phil', 'sarah'}
# for name in favorite_language.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#       language = favorite_language[name].title()
#       print(f"\t{name.title()}, I see you love {language}!")


#looping through a list in a particular order
# favorite_language = {
#     'sarah':'c',
#     'jen':'python',
#     'edward':'rust',
#     'phil':'python'
# }
# print("The following languages have been mentioned:")
# for language in favorite_language.values():
#     print(language.title())
# print()
# favorite_language = {
#     'sarah':'c',
#     'jen':'python',
#     'edward':'rust',
#     'phil':'python'
# }
# print("The following languages have been mentioned:")
# for language in set(favorite_language.values()):
#     print(language.title())


#6-3
# programming_words = {
#     'float':'It is a number with a decimal place \nexample "4.5"',
# 'boolean':'It is a value or expression that has only two states:\n"True/False"',
# 'string':'It is any value that is enclosed in a quotation: \n"yes"',
# "tuple":"It is an immutable list meaning it's contents can't be changed ",
# "dictionary":"It is a function that contains a key and value pair: 'key':'value'"
# }

# for key, value in programming_words.items():
#     print(f"{key}:{value}")


#6-5 river

river = {
    'ni'
}

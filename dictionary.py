import random

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

# rivers = {
#     "Nile": "Egypt",
#     "Amazon": "Brazil",
#     "Yangtze": "China",
#     "Mississippi": "United States",
#     "Congo": "Democratic Republic of Congo",
#     "Mekong": "China",
#     "Danube": "Germany",
#     "Ganges": "India",
#     "Euphrates": "Iraq",
#     "Indus": "Pakistan",
# }

# for key, value in rivers.items():
#     print(f"The {key} river runs through {value}.")
#     print("----------------------------------------------")

# for river in rivers.keys():
#     print(f"This is a river called: {river}.")
#     print("----------------------------------------------")

# for nations in rivers.values():
#     print(f"{nations} has a river somewhere.")
#     print("----------------------------------------------")


#already did a nested loop not completely but still did it

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
#     aliens.append(new_alien)

# for alien in aliens[0:10:2]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
    
# for alien in aliens[:10:3]:
#     if alien['color'] == 'green':
#          alien['color'] = 'red'
#          alien['points'] = 15
#          alien['speed'] = 'fast'

# for alien in aliens[:10]:
#     print(alien)
# print("......")

# favorite_languages = {
#     'jen': ['python','rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskell']

# }

# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#      print(f"\n{name.title()}'s favorite language is: ") 
#      for language in languages:
#         print(f"\t{language.title()}")
#     elif len(languages) == 2:
#      languages.pop(1)
#      print(f"\n{name.title()}'s favorite language is: ")
#      for language in languages:
#          print(f"\t{language.title()}")




#6-7

# users = {'AOthniel' : {
#      'first-name' : 'Othniel' ,
#      'last-name' : 'Ampofo',
#      'age' : 17 ,
#      'location' : 'west-fargo'
# },
# 'DJohn' : {
#      'first-name' :'John',
#      'last-name' : 'doe',
#      'age': 26,
#      'location': 'florida'
# },

# 'DMary' : {
#      'first-name' :'Mary',
#      'last-name' : 'doe',
#      'age': 23,
#      'location': 'florida'
# }
# }


# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first-name']} {user_info['last-name']}"
#     location = user_info['location']

#     print(f"\tFullname: {full_name}")
#     print(f"\tlocation: {location}")

# #6-8
# pet_list = {
#     'german shepherd': {
#         'pet_name' : 'peace',
#          'life_expecenty' : '9-16 years',
#          'age': 5
#     },
    
#     'bulldog': {
#         'pet_name' : 'luke',
#          'life_expecenty' : '8-10 years',
#          'age': 3
#     },

#     'husky': {
#         'pet_name' : 'joy',
#         'life_expecenty' : '12-15 years',
#         'age': 7
#     }

# }

# for breed, pet_info in pet_list.items():
#     print(f"\n Breed: {breed}")
#     name = pet_info['pet_name']
#     life_max = pet_info['life_expecenty']
#     current_age = pet_info['age']

#     print(f"\t NAME: {name}")
#     print(f"\t Life Expecenty: {life_max}")
#     print(f"\t Current Age: {current_age}")

#6-9


# name  = input("Enter your name:")
# while True:
#     location = input("Enter three locations you like: ")
#     list_location = [spot.strip() for spot in location.split(",")] 
#     if len(list_location) == 3:
#      break
# reason1 = input("Enter your reason:")
# name2 = input("Enter your name:")
# while True:
#     location1 = input("Enter three locations you like: ")
#     list_location1 = [spot.strip() for spot in location1.split(",")]
#     if len(list_location1) == 3:
#      break
# reason2 = input("Enter your reason:")
# name3 = input("Enter your name:")
# while True:
#     location2 = input("Enter three locations you like: ")
#     list_location2 = [spot.strip() for spot in location2.split(",")]
#     if len(list_location2) == 3:
#      break
# reason3 = input("Enter your reason:")
# main_location = [location, location1, location2]
# favorite_place = {
#    name:{
#       'location': main_location[0],
#       'reason' : reason1
#    },
#    name2:{
#       'location': main_location[1],
#       'reason' : reason2
#    },
#    name3:{
#       'location': main_location[2],
#       'reason': reason3
#    }
# }
# for keys, values in favorite_place.items():
#    print(f"{keys} said here are their favorite locations:")
#    print(f"\t{values}")


#6-10
# favorite number
# friends = ["Alice", "Bob", "Carlos", "Diana"]

# for friend in friends:
#   numbers = random.randint(1, 100)
#   print(f"{friend}'s favorite number is :\n{numbers }")


#6-11
# info_cities ={
#     'Cape Town':{
#         'country': ' South Africa',
#         "population": 5147000,
#         'fact' : " Cape Town is home to the world's first heart transplant," 
# "which was performed by Dr. Christiaan Barnard at Groote Schuur Hospital in 1967."
#     },
#     'Medellín':{
#         'country': 'Colombia',
#         'population': 4208000,
# 'fact': 'Transformed from a dangerous hub into a global leader in urban '
# 'innovation'

#     },
#     'Dakar': {
#         'country':'sengal',
#         'population': 3789000,
#         'fact': ' It is the westernmost city on the African mainland.'
#     }
# }
# cities = {
#     'Cape Town':info_cities['Cape Town'],
#     'Dakar':info_cities['Dakar'],
#     'Medellin': info_cities['Medellín']

# }
# for keys, data in cities.items():
#  print(f"Here is information about {keys}:\n\t{data}")

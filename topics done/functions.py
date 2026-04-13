import random
#defining a function
# def greeting_user():
#     print("Hello!")

# greeting_user()
#so that a function that was made to print a hello statement

# def age():
#     age = 17
#     print(f"You are {age} years old")

# age()
# this shows that a variable that is used as a function can be called in the function

#now we are gonna put in information through the parentheses
# def greeting_user(username):
#     print(f"Hello, {username.title()}")

# greeting_user('jesse')

#8-1 message
# def display_messsage():
#     prompt = "\nI have learnt about functions and how to call them,"
#     prompt += "\nNow i understand what functions are."
#     print(prompt)

# display_messsage()

# #8-2
# def favorite_book(title):
#     prompt = f"One of my favorite books is: {title}"
#     print(prompt)

# favorite_book('Alice in the wonderland')


# #positional functions
# def pet(animal_type, name):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type} is called: {name.title()}")

# pet('dog', 'harry')

#keyword arguments
# def pet(animal_type, name):
#     print(f"\nI have a {animal_type.title()}")
#     print(f"my {animal_type}'s name is:{name.title()}")

# #pet(animal_type='dog', 'harry')
# #SyntaxError: positional argument follows keyword argument
# # pet('harry', animal_type='dog')
# #TypeError: pet() got multiple values for argument 'animal_type'
# #so it should be 
# pet(animal_type='dog', name='harry')
#
#default value 
# def pet(name, animal_type='dog'):
#     print(f"\nI have a {animal_type.title()}.")
#     print(f"My {animal_type}'s name is: {name}")

# pet('johnny')
# #but python can overide that function if a argument is provided
# #example
# pet(animal_type='rabbit', name='johnny')

#8-3
# print T-shirt
# def detailed_shirt(size, message):
#   prompt = "Below are the information about your T-shirt:"
#   print(prompt)
#   print(f"Size:\n{size} \nMessage:\n\t{message}")
  
# Size = input("Enter the sizs you need for your T-shirt\nExample M,XL etc:")
# Message = input("Enter the message you want to be printed:")

# detailed_shirt(Size, Message)

#8-4
# def make_shirt(size,message):
#     prompt = "Below are the information about your T-shirt:"
#     print(prompt)
    
#     if size == 'L':
#         message = 'I love python'
#         print(f"Size:\n{size} \nMessage:\n\t{message}")
#     else:
#         print(f"Size:\n{size} \nMessage:\n\t{message}")

# Size = input("Enter the sizs you need for your T-shirt\nExample M,XL etc:")
# Message = input("Enter the message you want to be printed:")


# # make_shirt(message=Message, size=Size)
# prompt = "Enter a City and Country"
# print(prompt)

#return values

# def get_formatted_name(first_name, last_name):
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

# name = get_formatted_name('john', 'cage')
# print(name) 

#making an arugument optional
# def get_formatted_name(first_name,last_name, middle_name=''):
#     if middle_name:
#        full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name= f"{first_name} {last_name}"
#     return full_name.title()

# name = get_formatted_name('jimmy', 'hendrix')
# print(name)

# name =get_formatted_name('john', 'hooker', 'lee')
# print(name)

#returning a dicitionary 
# def build_person(first_name, last_name):
#     person = {'First_name':first_name, 'Last_name':last_name}
#     return person
# info = build_person('John', 'Doe')
# print(info)

# def getting_ready(first_name, last_number):
#     full_name = f"{first_name} {last_number}"
#     return full_name.title()


# active = True
# while active:
#     print("\nPlease enter your name:")
#     f_name = input("Enter your first name:")
#     if f_name == "quit" :
        
#         print("Quiting the Program.......")
#         break
#     else:
#          pass
#     l_name = input("Enter your last name:")
#     if l_name == "quit":
#          print("Quiting the Program.......")
#          active = False
#     else:
#           name = getting_ready(f_name,l_name)
#           print(f"Hello, {name}")
#8-6

# def city_format(city, country ):
#     city_formatted = f"{city.title()},{country.title()}"
#     return city_formatted

# active = True 
# prompt = "Enter a city and a Country."
# prompt = "\nEnter quit to exit."
# city_list = []
# country_list = []
# while active:
#     print(prompt)
#     city = input("Enter a city:") 
#     if city == "quit":
#        print("Quiting Program........")
#        for i in range(len(city_list)):
#         print(city_format(city_list[i],country_list[i]))
#         # for t in range(len(country_list)-1):
#         #  print(city_format(country_list[i]))
#        active = False
#     elif city != "quit":
#        country = input("Enter a country:")
#        city_list.append(city)
#        country_list.append(country)
       
#     else:
#        pass
     
     
     
#8-7
# #album
# def making_album(artist, album_title, songs= 0):
#     x , y, z  = artist, album_title, songs
#     dic = {
#         "aritist":x,
#         "ablum title":y,
#         "songs":z


#     }
#     # for aritist in dic['aritist'].items():     
#     # x = dic["aritist"].append(aritist)
#     # # for album_title in dic["ablum title"].items():
#     # y = dic['ablum title'].append(album_title)
#     # z = dic['songs'].append(songs)
#     return dic 

# print(making_album('john', 'lost', 10))


#8-8
#update to the ablum code
# def making_album(artist, album_title, songs=0):
#     dic = {
#         "artist": artist,
#         "album title": album_title,
#         "songs": songs
#     }
#     return dic


# prompt = "\nWelcome info.album"
# prompt += "\nEnter artist, album title, and songs."
# prompt += "\nEnter 'quit' at any time to exit."

# active = True

# while active:
#     print(prompt)

#     artist_info = input("Enter the artist: ")
#     if artist_info.lower() == "quit":
#         print("Quitting the program...")
#         break

#     album_info = input("Enter the album title: ")
#     if album_info.lower() == "quit":
#         print("Quitting the program...")
#         break

#     song_input = input("Enter number of songs: ")
#     if song_input.lower() == "quit":
#         print("Quitting the program...")
#         break

#     song_info = int(song_input)

#     album = making_album(artist_info, album_info, song_info)
#     print(album)

# passing a list 
# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)

# usernames = ['john', 'mike','james']
# greet_users(usernames)

#modifing the list in a function 
# unprinted_design = [ 'phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_design:
#     current_design = unprinted_design.pop()
#     print(f"Prining model: {current_design.title()}")
#     completed_models.append(current_design)
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model.title())



# 8-9 message
#my version
# def random_message():
#  messages = [
#         "Keep going, you are doing great.",
#         "Today is a perfect day to learn.",
#         "Believe in yourself and keep trying.",
#         "Small steps lead to big success.",
#         "Stay focused and never give up.",
#         "Your hard work will pay off.",
#         "Learning today builds success tomorrow.",
#         "Mistakes help you grow stronger.",
#         "Be patient, progress takes time.",
#         "You are becoming better every day.",
#         "Stay curious and keep learning.",
#         "Every challenge is a chance to improve.",
#         "Success starts with consistency.",
#         "You are stronger than you think.",
#         "Do not stop now, you are making progress.",
#         "Great things take time and effort.",
#         "Keep building your future one step at a time.",
#         "Confidence grows when you keep trying.",
#         "Your effort matters every single day.",
#         "Progress is still progress, no matter how small."
#     ]
#  return (random.choice(messages))
# print(random_message())


# random_message()

#8-10
#sending message
# def message():
#  messages = [
#         "Keep going, you are doing great.",
#         "Today is a perfect day to learn.",
#         "Believe in yourself and keep trying.",
#         "Small steps lead to big success.",
#         "Stay focused and never give up.",
#         "Your hard work will pay off.",
#         "Learning today builds success tomorrow.",
#         "Mistakes help you grow stronger.",
#         "Be patient, progress takes time.",
#         "You are becoming better every day.",
#         "Stay curious and keep learning.",
#         "Every challenge is a chance to improve.",
#         "Success starts with consistency.",
#         "You are stronger than you think.",
#         "Do not stop now, you are making progress.",
#         "Great things take time and effort.",
#         "Keep building your future one step at a time.",
#         "Confidence grows when you keep trying.",
#         "Your effort matters every single day.",
#         "Progress is still progress, no matter how small."
#     ]
#  return messages

# def sending_message():
#   sent_message = []
#   for info in message():
#    print(f"Current message:{info}")
#    print(".................................")
#    sent_message.append(info)
   
#   for sent in sent_message:
#     print(f"Sent Message:{sent}")

# sending_message()

# chatgpt version 
# messages = [
#     "Keep going, you are doing great.",
#     "Today is a perfect day to learn.",
#     "Believe in yourself and keep trying.",
#     "Small steps lead to big success.",
#     "Stay focused and never give up.",
#     "Your hard work will pay off.",
#     "Learning today builds success tomorrow.",
#     "Mistakes help you grow stronger.",
#     "Be patient, progress takes time.",
#     "You are becoming better every day.",
#     "Stay curious and keep learning.",
#     "Every challenge is a chance to improve.",
#     "Success starts with consistency.",
#     "You are stronger than you think.",
#     "Do not stop now, you are making progress.",
#     "Great things take time and effort.",
#     "Keep building your future one step at a time.",
#     "Confidence grows when you keep trying.",
#     "Your effort matters every single day.",
#     "Progress is still progress, no matter how small."
# ]

# def sending_message():
#     sent_messages = []

#     for msg in messages:
#         print(f"Current message: {msg}")
#         print(".................................")
#         sent_messages.append(msg)

#     print("\nAll sent messages:")
#     for sent in sent_messages:
#         print(f"Sent message: {sent}")

# sending_message()

#skipped 8-11 cuz it is kinda repeptitive 

#passing an arbitary of arguments
# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#      print(f"-{topping}")

# make_pizza("chesse","chicken")

# mixing positional ans arbitary arguments

# def make_pizza(size,*toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings
#         print(f"-{topping}")

# make_pizza(16,"chesse" ,"chicken")

#using arbitary Keyword arguments

# def build_profile(first, last, **user_info):
#     user_info['first-name'] = first
#     user_info['last-name']= last
#     return user_info

# user_info = build_profile('othniel', 'ampofo', location='north dakota',
#               city='west-fargo')
# print(user_info)

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
     
     
     

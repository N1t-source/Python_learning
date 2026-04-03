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


# make_shirt(message=Message, size=Size)
prompt = "Enter a City and Country"
print(prompt)


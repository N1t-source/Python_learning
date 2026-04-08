#cars.py
# cars = ['audi', 'bmw', 'lexus', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#      print(car.upper())
#     else:
#        print(car.title())

#Checking for inequality
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

#Numerical Comparisons
#magic number
# answer = 17

# if answer != 42:
#     print("That is not the correct answer, please try again")


#5-1 conditional tests
# car = 'subaru'
# print("Is car == 'subaru'? Ipredict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')


#if statements
#voting.py modified abit
# age = int(input("Enter Your age:"))
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print()

# age = int(input("Enter Your age:"))
# if age >= 18:
#      print("You are old enough to vote")
#      print("Have you registered to vote yet?")
# else:
#      print()



#if-else statments:
# age = int(input("Enter Your age:"))
# if age >= 18:
#       print("You are old enough to vote")
#       print("Have you registered to vote yet?")
# else:
#      print("Sorry, you are too Young to vote.")
#      print("Please register to vote as soon as you turn 18!")

# if-elif-else statements
# age = int(input("ENter your age:"))
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")


# age = int(input("Enter your age: "))
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f"Your admission cost is ${price}.")

#mutiple if-elif-else statement
# age = int(input("Enter your age: "))
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#  price = 40
# else:
#  price = 20
# print(f"Your admission cost is ${price}.")

# omitting the else block
# age = int(input("Enter your age: "))
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#  price = 40
# elif age >= 65:
#  price = 20
# print(f"Your admission cost is ${price}.")

#topping.py
# using a in function with if statement
# request_toppings =['mushroom', 'extra cheese']
# if 'mushroom' in request_toppings:
#     print("Adding mushrooms")
# if 'pepperoni' in request_toppings:
#     print("Adding pepperoni.")   
# if 'extra cheese' in request_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")


#5-3 Alien colors #1:
# alien_color = ['green', 'yellow', 'red']
# if 'green' in alien_color:
#     print("You have earned 5 points")
# if 'yellow' in alien_color:
#     print()
# if 'red' in alien_color:
#     print()

#5-3 advance version

# alien_color = str(input("Enter the color you recieved:"))
# if 'green' in alien_color:
#     print("You have earned 5 points")
# if 'yellow' in alien_color:
#     print()
# if 'red' in alien_color:
#     print()
#if alien_color != 'green' and alien_color != 'red' and alien_color !='yellow':
#     print("Invalid color input")

#5-4 Alien color
# alien_color = [ 'green','yellow', 'red']
# if 'green' in alien_color:
#     print("You have earned 5 points")
# else:
#     print("Yo have earned 10 points")

#5-5 Alien colors #3
# alien_color = str(input("Enter the color you recieved:"))
# if 'green' in alien_color:
#      print("You have earned 5 points")
# if 'yellow' in alien_color:
#      print("You have earned 10 points")
# if 'red' in alien_color:
#      print("You have earned 15 points")
#if alien_color != 'green' and alien_color != 'red' and alien_color !='yellow':
#      print("Invalid color input")


#5-6 stages of life
# name = input("Enter Your name:")
# age = int(input("Enter Your age:"))
# if age < 2:
#      print(f"{name} you are baby.")
# elif age >= 2 and age < 4:
#      print(f"{name}, you are a toddler.")
# elif age >= 4 and age < 13:
#      print(f"{name}, you are a kid.")
# elif age >= 13 and age < 20:
#      print(f"{name}, you are a teenager.")
# elif age >= 20 and age < 65:
#      print(f"{name}, you are an adult.")
# else:
#      print(f"{name}, you are an elder")

#5-7 Favorite friut
# fruit1 = input("Enter Your first favorite fruit:")
# fruit2 = input("Enter Your Second favorite fruit:")
# fruit3 = input("Enter Your least favorite fruit:")
# favorite_fruit = []
# favorite_fruit.append(fruit1)
# favorite_fruit.append(fruit2)
# favorite_fruit.append(fruit3)
# print(favorite_fruit)
# for fruit in favorite_fruit:
#     if fruit == fruit1:
#         print(f"{fruit} is really your favorite!")
#     if fruit == fruit2:
#         print(f"hmmmm i guess {fruit} is still your favorite.")
#     if fruit == fruit3:
#         print(f"{fruit} is your least favorite right.")
# if fruit1 in favorite_fruit and fruit2 in favorite_fruit:
#         print(f"{fruit1} and {fruit2}.\nYou have a really nice combo 😉.")
# if fruit3 in favorite_fruit and fruit2 in favorite_fruit:
#         print(f"{fruit3} and {fruit2}.\nHmmm 🤔 respect Your choice.")

#toppings.py 
# requested_toppings =['mushroom', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")


# requested_toppings = ['mushroom', 'green pepper', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green pepper':
#         print("Sorry, we are out of green peppers right now")
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")


#Checking that a list is not empty
# requested_toppings = []
# if requested_toppings:
#    for requested_topping in  requested_toppings:
#        print(f"Adding {requested_topping}.")
#    print("\nFinished making your pizza!") 
# else:
#     print("Are you sure you want a plain pizza?")

# Using multiple list
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
#                       'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping} toppings.")
# print("\nFinished making your pizza")


#5-8 Hello admin
# users = ['stacey', 'Mikey', 'Kobby', 'John', 'Admin']
# for user in users:
#     if 'Admin' in user:
#         print("Hello Admin, would you like to see stauts report?.")
#     else:
#         print(f"Hello {user}, thank you for logging again.")


#5-9 No user
# users = []
# if len(users) == 0:
#         print("We need to find some users") 
# else:
#   for user in users:
#    if 'Admin' in user:
#         print("Hello Admin, would you like to see stauts report?.")
#    else:
#         print(f"Hello {user}, thank you for logging again.")


#5-10 Checking Usernames:
# current_users = ['Stacey', 'Mikey', 'Kobby', 'John', 'Tory']
# copy_currentusers = []

# new_users = ['Stacey', 'othniel', 'peter'] 
# for user in current_users:
#  copy_currentusers.append(user.lower())
# for
# for user in new_users:
#  if user in copy_currentusers:
#   print(f"The Username {user} has already been used \nEnter a new user name.\n")
#  else: 
#   print(f"The Username {user} is available.")


#try 

# current_user = ['Stacey', 'Mikey', 'Kobby', 'John', 'Tory']
# copy_currentuser = []
# new_users = ['Stacey', 'othniel', 'peter'] 

# for user in current_user:
#     copy_currentuser.append(user.lower)

# for user in new_users:
#     if user.lower()  in copy_currentuser:
#         print(f"The Username {user} has already been used \nEnter a new user name.\n")
#     else:
#         print(f"The username {user} is available.")
    

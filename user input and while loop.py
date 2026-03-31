#parrot.py 
# message = input("Enter any message, and I will repeat it back to you:")
# print(message)

#greeter.py
# name = input("Please enter your name:")
# print(f"\nHello, {name}!")

# prompt = "if you share name, we can personalize the message you see."
# prompt +=  "\nWhat is your first name?"

# name = input(prompt)
# print(f"\nHello , {name}!")

#rollcoaster.py
# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou will be able to ride when you're little a bit older.")

# number = input("Enter a number, and i will tell if it is odd or even:")
# number = int(number)
# if number % 2 == 0:
#     print(f"The number {number} is even")
# else:
#     print(f"The number {number} is odd")

#7-1 rental car
# question = input("What rental car would you like?")
# if question.startswith("a "):
#  question = question[2:]
# print(f"\nLet me see if i can find you: a {question}")

# using break function in a while loop
# prompt = "\nEnter cities you would love to visit"
# prompt += "\nEnter 'quit' to stop the questions:"

# while True:
#     answer = input(prompt)
#     if answer == 'quit':
#         break
#     else:
#         print(f"I guess visiting {answer}, would be interesting.")
        

#using continue function in a while loop
# current_number = 0
# while current_number < 1000:
#     current_number += 1
#     if current_number % 3 == 0:
#         continue

#     print(current_number)


#pizza toppings
#7-4
# prompt = "\nEnter the topping your prefer"
# prompt += "\nEnter 'quit' to exit out this selection menu:"

# while True:
#     answer = input(prompt)
#     if answer == 'quit':
#         break
#     else:
#         print(f"{answer.title()} topping has been added.")

#7-5
#moive ticket price

# while True:
#     age = (input("\nEnter your age for your ticket price,\nEnter 'quit' to "
#     "exit:"))
#     try:
#         if age == 'quit':
#          break
#         elif int(age) >=0 and int(age) <=3:
#          print("Your ticket price is $0")
#         elif int(age) >=4 and int(age) <= 11:
#          print("Your ticket price is $10")
#         elif int(age) >=12 :
#          print("Your ticket price is $15") 
        
#     except ValueError: 
#          print(f"{age} isn't a vaild input, \nEnter only numbers:")


#7-6 three exits
#three different methods to exit
##pizza toppings
#7-4
# prompt = "\nEnter the topping your prefer"
# prompt += "\nEnter 'quit' to exit out this selection menu:"

# answer = ""
# while answer != 'quit':
#     answer = input(prompt)
#     if answer == 'quit':
#       print("Exit sucessful done!")
#     else:
#      print(f"{answer.title()} topping has been added.")

#7-5
#moive ticket price
#active = True
# while active:
#      age = (input("\nEnter your age for your ticket price,\nEnter 'quit' to "
#      "exit:"))
#      try:
#          if age == 'quit':
#           active = False
#          elif int(age) >=0 and int(age) <=3:
#           print("Your ticket price is $0")
#          elif int(age) >=4 and int(age) <= 11:
#           print("Your ticket price is $10")
#          elif int(age) >=12 :
#           print("Your ticket price is $15") 
        
#      except ValueError: 
#           print(f"{age} isn't a vaild input, \nEnter only numbers:")
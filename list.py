

#anime_list = ["To You Eternity", "MHA", "JJK", "OPM"]
#print(anime_list)

#Accesing Elements in a list
#print(anime_list[0])
#print(anime_list[3].title())

#Using Individual Values from a list
#message = f"My favorite Anime is {anime_list[2].title()}"
#print(message)


#3-1 Names
#names = ["John", "Martin", "Oda", "kelvin"]
#print(names[0].title())
#print(names[1].title())
#print(names[2].title())
#print(names[3].title())

#3-2
#message = " What's up,"
#print(f"{message} {names[0].title()}")
#print(f"{message} {names[1].title()}")
#print(f"{message} {names[2].title()}")
#print(f"{message} {names[3].title()}")

#3-3
#items = ["Apple", "Icecream", "Iphone", "Python crash course Book", "bottle"]
#message = "I would like to own "
#print(f"{message.rstrip()}, An {items[0].title()}")
#print(f"{message.rstrip()}, An {items[1].title()}")
#print(f"{message.rstrip()}, An {items[2].title()}")
#print(f"{message.rstrip()}, A {items[3].title()}")
#print(f"{message.rstrip()}, A {items[4].title()}")

#Modifying , Adding and Removing Elements

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

#Adding Elements to a List

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#
#motorcycles.append('ducati')
#print(motorcycles)


#motorcycles = []
#motorcycles.append('ducati')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')
#motorcycles.append('honda')

#print(motorcycles)

#Removing an item Using the del statment
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)


#Removing an item using the pop() method
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)

#last_owned = motorcycles.pop()
#print(f"The last motor i owned was a {last_owned.title()}.")


#Popping items from Any Position in a list 
#motorcycles = ['honda', 'yamaha', 'suzuki']
#first_owned = motorcycles.pop(0)
#print(motorcycles)
#print(f"The first Motor I owned was a {first_owned.title()}.")

#Removing an item by value
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)
#motorcycles.remove('ducati')
#print(motorcycles)

#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)

#too_expensive = 'ducati'
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print(f"\nA {too_expensive} is too expensive for me.")

#Guest List 
#invited_guest = ['John', 'Aaron', 'Alan', 'Martin']
#guest1 = invited_guest.pop(0)
#print(f"Hi there, {guest1}")
#guest2 = invited_guest.pop(1)


#Organizing a list 
#sorting a list permanently with the sort() Method
#cars = ['bmw', 'lexus', 'audi', 'lambo', 'dodge']
#print(cars)
#cars.sort()
#print(cars)

#cars.sort(reverse=True)
#print(cars)

#Sorting a list Temporarily with the sorted() function
#cars = ['bmw', 'lexus', 'audi', 'lambo', 'dodge']
#print("Here is the original list:")
#print(cars)

#print("\nHere is the sorted list:")
#print(sorted(cars))

#print("\nHere is the original list again:")
#print(cars)

#Printing a list in reverse order
#cars = ['bmw', 'lexus', 'audi', 'lambo', 'dodge']
#print(cars) 
#cars.reverse()
#print(cars)


# Finding the lenght of a list 
#cars = ['bmw', 'lexus', 'audi', 'lambo', 'dodge']
#print(cars)
#length = len(cars)
#print(length) 


#3-8
#visits =  ['Kyoto', 'berlin', 'Dubai', 'Ghana']
#print("Here is the orginal list:")
#print(f"{visits}\n")

#print("Here is the sorted list: ")
#print(f"{sorted(visits)}\n")

#print("Here is the orginal list again:")
#print(f"{visits}\n")
#visits.reverse()
#print("Here is the sorted reverse list:")
#print(f"{sorted(visits)}\n")
#visits.reverse()
#print("Here is the orginal list again:")
#print(f"{visits}\n")

#visits.sort()
#print("Here is the sorted list again:")
#print(f"{visits}\n")
#visits.sort()
#visits.reverse()
#print("Here is the sorted reverse list:")
#print(f"{visits}\n")

#3-10
#Every fucntion
#question = input("What do you want to make a list about:")
#list2 = question
#print(list2)
#list1 = []
#while True:
 #question2 = input("\nEnter one by one:")
# list1.append(question2)
# if len(list1) == 3:
#  print("Ok your list is complete.")
#  break
# else:
#  print(f"Continue {(3 - len(list1))} more ")
#print(f"Here are the {list2} list:")  
#print(list1)

#print(f"Now Here are the {list2} sorted and popped seperately:")

#sorted_list = sorted([item.title() for item in list1])
#print(f"Here lies the sorted {question} list:\n{sorted_list}")
#popped_list = (f"{list1.pop(0)}\n{list1.pop(1)}\n{list1.pop()}")
#print(f"Here lies the popped {question} list:\n{popped_list}")
 

# Working with list 
#loop

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#    print(magician)

#dashes = ('------------------------------------')
#print(dashes)

#magicians = ['john', 'mike', 'martin','carolina']
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")

#dashes = ('-------------------------------------')
#print(dashes)

#magicians = ['john', 'mike', 'martin','carolina']
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I can't wait to see your next trick, {magician.title()}.\n{dashes}")


#print("Thank you everyone, that was a great magic show")

#4-1
#pizza
#dashes = ('-------------------------------------')
#pizzas = ['bianca', 'meat lovers', 'bbq chicken']

#for pizza in pizzas:
#    print(f"I like {pizza.title()} pizza")
#    print(dashes)

#print(f"{pizzas} are the pizzas i like")


#4-2
#Animals
# animals = ['dog', 'cat', 'horse']
# for animal in animals:
#     print(f"A {animal.title()} would make a great pet")
# print("Any of these animals, would make a great pet")

#using the range() function

# for value in range(1, 5):
#  print(f"{value}")

# for value in range(1, 6):
#  print(value)

# for value in range(8):
#  print(value)

#Using range() to Make a list of Numbers
# numbers = list(range(1, 6))
# print(numbers)

# numbers = list(range(1, 7))
# for number in numbers:
#     print(number)

#Even numbers and odd numbers
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# odd_numbers = list(range(1, 12, 2))
# print(odd_numbers)

#Squaring function
# squares = []
# for values in range(1, 13):
#     square = values ** 2
#     squares.append(square)

# print(squares) 

# More efficent method
# squares = []
# for values in range(1, 13):
#     squares.append(values ** 2)

# print(squares)

#//Simple Statistics with a list of numbers
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0]
# print(digits)
# print(min(digits))
# print(max(digits))
# print(sum(digits))


#List comprehensions
# this uses only one line of code to invoke a list
# squares = [value**2 for value in range(1, 13)]
# print(squares)

#Execrises
#4-3
# print("This is a count function:")
# for number in range(1, 21):
#  print(number)
# print("The End ")

#4-4 counting to a million
# to_million = []
# for values in range(1, 1000001):
#     to_million.append(values)
# for value in to_million:
#     print(value)

#4-5 summing a million digits
# digits = []
# for value in range(1, 1000001):
#     digits.append(value)
# print(min(digits))
# print(f"{max(digits):,}")
# print(f"{sum(digits):,}")


#4-6 odd numbers
# odd_numbers = []
# for numbers in range(1, 21, 2):
#     odd_numbers.append(numbers)
# print("This is a list of odd numbers:")    
# print(odd_numbers)


#4-7 multiples of N number
# multiple = float(input("\nEnter the number You want to see a multiple of:"))
# N = []
# for multiples in range(1, 21):
#     N.append(int(multiples*multiple))
# print(f"This is a multiple of {multiple}, \nFrom 1-20.")
# print(N)


# 4-8 Cube function
# cubes = []
# for cube in range(1, 11):
#     cubes.append(cube**3)
# print(cubes)


#4-9 Cube function using a list comprehension
# Cubes = [value**3 for value in range(1, 11)]
# print(Cubes)


# Working with part of a list
#Slicing a list

# player = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(f'{player[0:3]}\n')
# print(f'{player[1:4]}\n')
# print(f'{player[2:5]}\n')
# print(f'{player[:4]}\n')
# print(f'{player[-3:]}\n')

#LOOPING THROUGH A SLICE
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first players on my team:")
# for player in players[:3]:
#     print(player.title())

#COPYING A LIST 
# my_food = ['pizza', 'rice', 'cake', 'falafel']
# friend_food = my_food[:]

# print("My favorite foods are:")
# print(my_food)

# print("\nMy friend's favorite food are:")
# print(friend_food)


# my_foods = ['pizza', 'rice', 'cake', 'falafel']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('Ice cream')
# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite food are:")
# print(friend_foods)



#4-10 
#Slices

# first_list = ['Gym', 'Running', 'Sports']
# print("The first three items in the list are:")
# for items in first_list[:]:
#     print(items)

# print(f"Here are all the {len(items)} in the list")




# second_list = ['Cars', 'Money', 'Games']
# print("Three items for the middle list are:")
# for items in second_list[:]:
#     print(items)


# third_list = ['football', 'scocer', 'basketball']
# print("The last three items in the list:")
# for items in third_list[:]:
#     print(items)


#4-11 My pizza ,your pizza
# dashes = ('-------------------------------------')
# my_pizza = ['bianca', 'meat lovers', 'bbq chicken']
# friends_pizza = my_pizza[:]

# print(my_pizza)
# print(friends_pizza)
# my_pizza.append('pineapple')
# friends_pizza.append('chesse')

# for pizza in my_pizza:
#     print(f"I like {pizza.title()} pizza.")
# print(dashes)

# for pizza in friends_pizza:
#     print(f"My friend likes, {pizza.title()} pizza.")

# print(f"{my_pizza} are the pizzas i like\nAnd")
# print(f"{friends_pizza} are the pizzas he likes")



#4-12 Food.py loop function
dashes = ('-------------------------------------')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]
print("My favorite foods are:")
for food in my_foods:
    print(food)
print(dashes)
print("\nMy friend's favorite foods are:")
for food in reversed(friend_food):
    print(food)

# dimensions.py
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

#Error when trying tom modify the list made with a tuple
# dimensions = (200, 50)
# dimensions[0] = 250

#  look     
# dimensions[0] = 250
#     ~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

#Looping through All values in a tuple
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)


# Writing over a tuple
# dimensions = (200, 50)
# print("Orginal  dimension:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions: ")
# for dimension in dimensions:
#     print(dimension)


#4-13
#Buffet

# buffet = ('Chicken mac nut', 'hot dog party', 'sugar rush', 'stomach crucher', 'pizza sunday')
# print("Here is the Buffet menu:")
# for item in buffet:
#     print(item)
# # buffet.remove('pizza sunday')
# # print(buffet)

# buffet = ('Chicken mac nut', 'hot dog party', 'rush soda', 'Creamy friday', 'pizza sunday')
# print("\nHere is the revised Menu:")
# for item in buffet:
#     print(item)

#Experiment with tuples
#buffet = ('Chicken mac nut', 'hot dog party', 'rush soda', 'Creamy friday', 
#'pizza sunday')
# copy_buffet = buffet[:]
# for item in copy_buffet:
#     print(item)


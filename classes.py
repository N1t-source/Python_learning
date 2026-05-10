# class Dog:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
    
#     def sit(self):
#         print(f"{self.name} is now sitting ")
    
#     def roll_over(self):
#         print(f"{self.name} rolled over")

# dog = Dog("john", 2)
# sit = dog.sit()
# sit = dog.roll_over()

#9-1 Restaruant 

# class Restaruant:
#     def __init__(self,name,cuisine,open):
#         self.name = name
#         self.cuisine = cuisine
#         self.open = open
#     def restaruant_name(self):
#         print(f"Welcome to {self.name} Restaruant!")

#     def describe_restaruant(self):
#         print(f"{self.name} is a five star restaruant, We serve alot of Gourmet"
#               "\nThe only place with nice meals")
        
#     def open_restaruant(self):
#         if self.open == True:
#             print(f"{self.name} is now, opened!")
#         else:
#             print(f"Sorry {self.name} isn't opened currently")

#     def lines(self):
#         print("------------------------------------")

# restaruant1 = Restaruant("KFC","Fried rice",False)
# r1 = restaruant1.restaruant_name()
# r1 = restaruant1.describe_restaruant()
# r1 = restaruant1.open_restaruant()
# r1 = restaruant1.lines()
#  # 9-2 creating like three calls
# restaruant2 = Restaruant("Juspizza","Pizza",True)
# r2 = restaruant2.restaruant_name()
# r2 = restaruant2.describe_restaruant()
# r2 = restaruant2.open_restaruant()
# r2 = restaruant2.lines()


# restaruant3 = Restaruant("Mcdonalds","Buger",False)
# r3 = restaruant3.restaruant_name()
# r3 = restaruant3.describe_restaruant()
# r3 = restaruant3.open_restaruant()
# r3 = restaruant3.lines()


# restaruant4 = Restaruant("Lemon's lime","lime juice",True)
# r4 = restaruant4.restaruant_name()
# r4 = restaruant4.describe_restaruant()
# r4 = restaruant4.open_restaruant()
# r4 = restaruant4.lines()


#9-3 User class
# class User:
#     def __init__(self,name=str,gender=str,age=int,active=bool):
#         self.name = name 
#         self.gender = gender
#         self.age = age 
#         self.active = active 
#     def describe_user(self):
#         self.user_name()
#         self.user_gender()
#         self.user_age()
#         self.user_active()

#     def user_name(self):
#         print(f"Welcome User:{self.name}\nHow you feeling today XD")

#     def user_gender(self):
#         print(f"The Gender of User,{self.name} is a {self.gender}")

#     def user_age(self):
        
#         print(f"User: {self.name} is {self.age} years old")

#     def user_active(self):
#         if  self.active == True:
#          print(f"The User's account is active")
#         else:
#             print(f"The account isn't active")

#     def lines(self):
#          print("------------------------------------")

# john = User("Rocky","MALE",20,True)
# # user = john.user_name()
# # user = john.user_gender()
# # user = john.user_age()
# # user = john.user_active()
# # user = john.lines

# user = john.describe_user()

#creating a Car class
# class Car:
#     def __init__(self,make,model,year=int):
#         self.make = make
#         self.model = model 
#         self.year = year 
    
#     def get_descriptive_name(self):
#         long_name  = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

# my_car = Car("audi", 'a4',2025)
# print(my_car.get_descriptive_name())

#setting a default value for an attribute 
class Car:
    def __init__(self,make,model,year):
        self.make = make 
        self.model = model
        self.year = year 
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} mile on it.")

my_new_car = Car("audi","a4",2024)
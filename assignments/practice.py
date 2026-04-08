# prompt = "\nWelcome to Odessy Bank"


# accounts = {
#     'alice':{
#         'pin': '1234',
#         'balance': 500.00
#         },
            
#     'bob':{
#         'pin': '5678',
#         'balance': 150.00
#     }
# }
# #prompt += "\nEnter your username to login"
# print(prompt)
# username = input("Enter your username to login:")

# prompt1 = f"\nHi {username}, welcome to Odessy bank. "
# prompt1 += "\nCan you kindly enter your pin to confirm, "
# prompt1 += "\n Your identity. "
# print(prompt1)
# attempts = 0
# while attempts != 3:
#     pin = input("Enter the pin code:")
#     if pin == accounts[username]['pin']:
#         print("Login successful")

#         while True:
#             print("\nWhat would you like to do?")
#             print("1. check balance")
#             print("2. Deposit")
#             print("3. Withdrawal")
#             print("4. Logout")
#             try:
#              choice  = int(input("Enter your choice:"))
#             except ValueError:
#                 print("Invaild choice. please try again")
#                 continue
#             if choice == 1:
#                 print(f"Your balance is: ${accounts[username]["balance"]}")
#             elif choice == 2:
#                 amount = float(input("Enter only figures:"))
#                 accounts[username]['balance'] = accounts[username]['balance'] + amount
                
#                 print(f"Your new balance is ${accounts[username]['balance']}")
#             elif choice  == 3:
#                 withdrawal = float(input("Enter an amount to withdraw:"))
#                 if withdrawal > accounts[username]['balance']:
#                     print(f"Operation was not successful,\n${withdrawal} was high.")
#                 else:
#                     print(f"${withdrawal} was successfully withdrawn.")
#                     print(f"Current balance is:{accounts[username]['balance'] - withdrawal}")
#             elif choice  == 4:
#                 break
#         break
#     else:
#         attempts += 1
# if attempts == 3:
#     print("Account locked!")
 



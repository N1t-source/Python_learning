
#name = "othniel darling-ampofo"
#print(name.title())
#print(name.upper())
#print(name.lower())


#using variables in strings
#first_name = "othniel"
#middle_name = "darling"
#last_name = "ampofo"
#full_name = f"{first_name} {middle_name} {last_name}"
#print(full_name)
#message = f"Hello, {full_name.title()}!"
#print(message)

#Adding whitespace to strings with tabs or newlines
#\t which add a tab to your text
#print("Python")
# Vs
#print("\tPython")

#\n adds a newline  in string 
#print("Languages:\nPython\nC++\nJavascript")
# Vs
#\t
#print("languages:\tPython,\tC++,\tJavascript")
#print("Which is better")

#combining \t with \n
#print("languages:\n\tPython\n\tC++\n\tJavascript")

#stripping Whitespace
#favourite_language = "    'Python     "
#print(favourite_language)
#print(favourite_language)
#favourite_language  = favourite_language.lstrip()
#favourite_language  = favourite_language.lstrip().rstrip()
#favourite_language = favourite_language.rstrip()
#favourite_language

#comment: honestly i dont see anything in my terminal  

#print(favourite_language)
#update comment i do see some changes when i invoke the lstrip function for the white space in the left side


#Removing Prefixes 
#nostarch_url = "https://nostarch.com"
#print(nostarch_url)
#simple_url = nostarch_url.removeprefix("https://")
#print(simple_url)

#Avoiding Syntax Errors
#message = "One of Python's Strengths is its diverse community"
#print(message)

#message = "One of Python's Strengths is its diverse community"

# it will print an error watch just change all to single quotes
#print(message)

#Personal Messagge 
#2-3
#name = "Othniel"
#print(f"Hello {name}, would you like to learn Python Today")

#2-4 Name case
#comment: so personal i know how to use input() function
#so am gonna utilize it 
#name = input("Enter Your Name:")
#name = name.title()
#print(name)
#name = name.upper()
#print(name)
#name = name.lower()
#print(name)


#2-5 Famous qoutes 
#simple version
#message = 'Albert Einstein once said, \n\t\t\t"A person who never made a mistake never tried anything new" '
#print(message)


#advanced version
#famous_person = "Malcom X"
#message = '"The future belongs to those who prepare for it today"
#print(f"{famous_person} once said, \n\t\t{message}")


#Stripping name
#name = " Othniel\tDarling\tAmpofo  "
#print(name)
#name = name.lstrip()
#print(name)
#name = name.rstrip()
#print(name)
#name = name.strip()
#print(name)


#File Extention
#file_type = "Python_course.txt"
#print(file_type)
#file_type = file_type.removesuffix(".txt")

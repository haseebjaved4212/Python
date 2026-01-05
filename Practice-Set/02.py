# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Enter your name: ")
print("Good Afternoon", name)


# 2. Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>,
Greetings from ABC coding house. I am happy to tell you about the selection.
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|Date|> '''

name = input("Enter your name: ")
date = input("Enter date: ")

print(letter.replace("<|Name|>", name).replace("<|Date|>", date)) 

# 3. Write a python program to detect double spaces in a string.

string = input("Enter a string: ")
if "  " in string:  print("Double spaces detected.")
else:   print("No double spaces detected.")


# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n\tThis Python course is nice.\nThanks!"
print(letter)

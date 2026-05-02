# Q1: Accept an integer and print Hello world n times 

"""
n = int(input("Enter an integer: "))
for i in range(n):
    print("Hello World")  
"""

# Q2: Print the  natural numbers up to n ?

"""
n = int(input("Enter an integer: "))
for i in range(1, n + 1):
    print(i)

"""

# Q3: Reverse a String Without Using Built-in Functions

# a = input("Enter a string: ")

# for i in range(len(a)-1, -1, -1):
#     print(a[i], end="")

#  Q4 : Check if the String is Palindrome or not?
# First of all, we need to understand what a palindrome is. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).


# a = "Haseeb"
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
  
# if a == b:
#     print("The string is a palindrome.")    
# else:    print("The string is not a palindrome.")


# Q5 : Count all the digits, letters and special characters in a string?

# a = input("Enter a string with special characters, digits and letters: ")
# digits = 0    
# letters = 0
# special_characters = 0
# for i in a:
#     if i.isdigit():
#         digits += 1
#     elif i.isalpha():
#         letters += 1
#     else: 
#         special_characters += 1
# print(f"Digits: {digits}\nSpecial Characters: {special_characters}\nLetters: {letters}")


# While Loop

# Q1: separate each digit of a number and print them in a new line?
# n = int(input("Enter an integer: "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# print(rev)

#  Q2: Check if the given number is palindrome or not?

# n = int(input("Enter an integer: "))
# rev = 0
# temp = n
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if temp == rev:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")


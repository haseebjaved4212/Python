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

a = input("Enter a string: ")

for i in range(len(a)-1, -1, -1):
    print(a[i], end="")



# Text to Speech Conversion using pyttsx3

# import pyttsx3
# engine = pyttsx3.init ()

# engine.say ("Hey I am Haseeb, I am learning Python.")
# engine.runAndWait ()


# List Files in a Directory using os module

import os

# Specify the directory path
directory_path = "/"

# List all files and folders in the directory
contents = os.listdir(directory_path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)
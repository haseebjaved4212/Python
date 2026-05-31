from pathlib import Path

def readFileAndFolder():
  path = Path('')
  items = list(path.rglob('*'))
  for i, items in enumerate(items):
    print(f"{i+1 }: {items}") 



# Creating a file:
def createFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with p.open(mode='w') as fs:
                data = input("Enter the data you want to write in the file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY!")
        else:
            print("File already exists!")
    except Exception as err:
        print(f"An error occurred: {err}")



#  reading a File:
def readFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with p.open(mode='r') as fs:
                data = fs.read()
                print(f"Data in the file: {data}")
        else:
            print("File does not exist!")
    except Exception as err:
        print(f"An error occurred: {err}")


def updateFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 to updating your file name: ")
            print("Press 2 to overwriting the file:")
            print("Press 3 to appending some content to the file:")

            res = int(input("Enter your choice: "))
            if res == 1:
                newName = input("Enter the new name of the file: ")
                p.rename(newName)
                print("File name updated successfully!")
            if res == 2:
                with p.open(mode='w') as fs:
                    data = input("Enter the data you want to write in the file: ")
                    fs.write(data)
                print("File updated successfully!")
            if res == 3:  
                with p.open(mode='a') as fs:
                    data = input("Enter the data you want to append to the file: ")
                    fs.write(data)
                print("File updated successfully!")
        else:
            print("File does not exist!")
    except Exception as err:
        print(f"An error occurred: {err}")



def deleteFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully!")
        else:
            print("File does not exist!")
    except Exception as err:
        print(f"An error occurred: {err}")






















print("Press 1 to create a file")
print("Press 2 to Read a file")
print("Press 3 to Update a file")
print("Press 4 to Delete a file")

check = int(input("Enter your choice: "))

if check == 1:
  createFile()

if check == 2:
  readFile()

if check == 3:
  updateFile()

if check == 4:
  deleteFile()
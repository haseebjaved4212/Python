from pathlib import Path

def readFileAndFolder():
  path = Path('')
  items = list(path.rglob('*'))
  for i, items in enumerate(items):
    print(f"{i+1 }: {items}") 



def createFile():
          readFileAndFolder()
          name = input("Enter the name of the file you want to create: ")
          p = Path(name)
          with p.open(mode='w') as fs:
            data = input("Enter the data you want to write in the file: ")
            fs.write(data)
print("FILE CREATED SUCCESSFULLY!")


print("Press 1 to create a file")
print("Press 2 to Read a file")
print("Press 3 to Update a file")
print("Press 4 to Delete a file")

check = int(input("Enter your choice: "))

if check == 1:
  createFile()
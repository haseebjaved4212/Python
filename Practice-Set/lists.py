# Q1: Print the largest number in the list and its index.

l = [3, 5, 7, 2, 8, 1]
largest = l[0]
index = 0

for i in range(1, len(l)):
    if l[i] > largest:
        largest = l[i]  
        index = i
print(f"Largest number: {largest} at the Index: {index}")


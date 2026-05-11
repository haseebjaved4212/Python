# Q1: Print the largest number in the list and its index.

# l = [3, 5, 7, 2, 8, 1]
# largest = l[0]
# index = 0

# for i in range(1, len(l)):
#     if l[i] > largest:
#         largest = l[i]  
#         index = i
# print(f"Largest number: {largest} at the Index: {index}")

# Q2: Print the second largest number in the list and its index.

l = [3, 5, 7, 2, 8, 1]
largest = l[0]
second_largest = l[0]
index = 0

for i in range(1, len(l)):
    if l[i] > largest:
        second_largest = largest
        largest = l[i]
        index = i 
    elif l[i] > second_largest and l[i] != largest:
        second_largest = l[i]
print(f"Second largest number: {second_largest} at the Index: {l.index(second_largest)}")
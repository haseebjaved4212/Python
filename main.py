# print("Hello, World!")

# For loop

# for i in range(5,1 , -1):
#     print(i)


n = int(input("Which table you wanna print : "))

for i in range(n , n*10 + 1, n):
    print(i)

"""
Optimizing tool selection...# Code Logic Explanation

Your code prints a **multiplication table** for a given number. Here's how it works:

```python
n = int(input("Which table you wanna print : "))
```
- Takes input from the user and converts it to an integer
- Stores it in variable `n`

```python
for i in range(n , n*10 + 1, n):
    print(i)
```
 - **Loop**: `for i in range(n, n*10 + 1, n)`
  - **Start**: `n` (begins from the input number)
  - **End**: `n*10 + 1` (goes up to 10 times the number)
  - **Step**: `n` (increments by `n` each iteration)
- **Print**: `print(i)` outputs each value

## Example
If user inputs `5`:
- Range: `range(5, 51, 5)` 
- Output:
  ```
  5
  10
  15
  20
  25
  30
  35
  40
  45
  50
  ```

This effectively prints the **multiplication table of n from 1×n to 10×n**.
"""
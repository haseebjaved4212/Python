# 🔁 Python Loops — Complete Reference

> A deep dive into every loop construct Python has to offer — from basic iteration to advanced control flow patterns.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-12-orange?style=flat-square)
![Examples](https://img.shields.io/badge/Code%20Examples-40+-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

---

## 📚 Table of Contents

1. [What is a Loop?](#1-what-is-a-loop)
2. [The `for` Loop](#2-the-for-loop)
3. [The `while` Loop](#3-the-while-loop)
4. [Loop Control Statements](#4-loop-control-statements)
5. [Nested Loops](#5-nested-loops)
6. [Looping with Built-in Functions](#6-looping-with-built-in-functions)
7. [List Comprehensions](#7-list-comprehensions)
8. [Dictionary & Set Comprehensions](#8-dictionary--set-comprehensions)
9. [Iterators & Iterables](#9-iterators--iterables)
10. [The `else` Clause on Loops](#10-the-else-clause-on-loops)
11. [Performance & Best Practices](#11-performance--best-practices)
12. [Quick Reference Cheat Sheet](#12-quick-reference-cheat-sheet)

---

## 1. What is a Loop?

A loop lets you **execute a block of code repeatedly** without writing it multiple times. Instead of copy-pasting the same logic ten times, you write it once and let the loop do the work.

Python has two types of loops:

| Loop | Use When |
|------|----------|
| `for` | You know what you are iterating over (a list, range, string, etc.) |
| `while` | You repeat until a condition becomes `False` and don't know the count upfront |

```python
# Without a loop — repetitive and unscalable
print(1)
print(2)
print(3)
print(4)
print(5)

# With a loop — clean and scalable
for i in range(1, 6):
    print(i)
```

---

## 2. The `for` Loop

The `for` loop iterates over any **iterable** — a list, tuple, string, dictionary, range, or any object that supports iteration. Python handles the counter automatically.

### Basic Syntax

```python
for variable in iterable:
    # code block runs once per item
```

### Iterating Over Common Types

```python
# List
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# String — iterates character by character
for char in "Python":
    print(char)

# Tuple
coords = (10, 20, 30)
for val in coords:
    print(val)

# Range — most common for counted loops
for i in range(5):       # 0 1 2 3 4
    print(i)

for i in range(1, 6):    # 1 2 3 4 5
    print(i)

for i in range(0, 10, 2):  # 0 2 4 6 8  (step = 2)
    print(i)

for i in range(10, 0, -1): # 10 9 8 ... 1 (countdown)
    print(i)
```

### `range()` Parameters

```python
range(stop)              # range(5)       → 0, 1, 2, 3, 4
range(start, stop)       # range(2, 6)    → 2, 3, 4, 5
range(start, stop, step) # range(0, 10, 3)→ 0, 3, 6, 9
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `start` | Where to begin (inclusive) | `0` |
| `stop` | Where to end (exclusive) | required |
| `step` | How much to increment | `1` |

### Iterating Over a Dictionary

```python
person = {"name": "Haseeb", "role": "dev", "lang": "Python"}

# Keys only (default)
for key in person:
    print(key)

# Values only
for value in person.values():
    print(value)

# Both keys and values
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 3. The `while` Loop

The `while` loop keeps running **as long as a condition is `True`**. You are responsible for updating whatever drives that condition, otherwise you get an infinite loop.

### Basic Syntax

```python
while condition:
    # code block
    # update something that affects the condition
```

### Simple Counter

```python
count = 0
while count < 5:
    print(count)
    count += 1   # without this, infinite loop!
# Output: 0 1 2 3 4
```

### User Input Validation

This is a classic `while` use case — you keep asking until the user gives valid input.

```python
while True:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) > 0:
        print(f"Age accepted: {age}")
        break
    print("Invalid input. Try again.")
```

### Countdown Timer

```python
import time

seconds = 5
while seconds > 0:
    print(f"Starting in {seconds}...")
    time.sleep(1)
    seconds -= 1
print("Go!")
```

### Polling / Retry Pattern

```python
import random

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    success = random.choice([True, False])
    attempts += 1
    if success:
        print(f"Connected on attempt {attempts}")
        break
    print(f"Attempt {attempts} failed, retrying...")
else:
    print("Could not connect after max attempts")
```

> [!WARNING]
> Always make sure something inside your `while` loop moves you closer to the exit condition. A forgotten increment or a condition that can never turn `False` causes an **infinite loop** that freezes your program.

---

## 4. Loop Control Statements

These three keywords let you take control of how a loop runs mid-execution.

### `break` — Exit the Loop Immediately

```python
numbers = [1, 3, 7, 2, 9, 4, 6]

for num in numbers:
    if num == 2:
        print(f"Found 2! Stopping.")
        break
    print(num)

# Output: 1 3 7
# Found 2! Stopping.
```

### `continue` — Skip Current Iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)

# Output: 1 3 5 7 9
```

### `pass` — Do Nothing (Placeholder)

```python
for i in range(5):
    if i == 3:
        pass   # placeholder — will handle this later
    print(i)

# Output: 0 1 2 3 4
# pass does nothing, loop continues normally
```

### Summary Table

| Statement | Effect | Loop Continues? |
|-----------|--------|----------------|
| `break` | Exits the loop entirely | No |
| `continue` | Skips the rest of the current iteration | Yes, next iteration |
| `pass` | Does nothing, acts as a placeholder | Yes, same iteration |

### Nested Loop with `break`

```python
# break only exits the INNERMOST loop it is in
for i in range(3):
    for j in range(3):
        if j == 1:
            break       # exits inner loop only
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=1, j=0
# i=2, j=0
```

---

## 5. Nested Loops

A loop inside another loop. The inner loop completes all its iterations for every single iteration of the outer loop.

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")
```

### Iterating a 2D List (Matrix)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()   # newline after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### Pattern Printing

```python
# Right triangle
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# Output:
# *
# **
# ***
# ****
# *****
```

> [!TIP]
> Be careful with deeply nested loops. Three or more levels of nesting is usually a sign you should refactor — extract the inner loop into a separate function to keep things readable.

---

## 6. Looping with Built-in Functions

Python ships with powerful built-ins that make loops cleaner and more expressive.

### `enumerate()` — Loop with Index

```python
fruits = ["apple", "banana", "mango"]

# Without enumerate — clunky
for i in range(len(fruits)):
    print(i, fruits[i])

# With enumerate — clean and Pythonic
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Start index at 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

### `zip()` — Loop Over Multiple Iterables

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]
grades = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")

# Output:
# Alice: 88 (B)
# Bob: 95 (A)
# Charlie: 72 (C)
```

> [!NOTE]
> `zip()` stops at the shortest iterable. Use `itertools.zip_longest()` if you need to handle iterables of different lengths.

### `reversed()` — Iterate Backwards

```python
items = [1, 2, 3, 4, 5]

for item in reversed(items):
    print(item)
# Output: 5 4 3 2 1
```

### `sorted()` — Iterate in Sorted Order

```python
scores = [72, 95, 88, 61, 100]

for score in sorted(scores, reverse=True):
    print(score)
# Output: 100 95 88 72 61
```

### `map()` — Apply a Function to Each Item

```python
numbers = [1, 2, 3, 4, 5]

# Apply a function to every element
squared = list(map(lambda x: x**2, numbers))
print(squared)   # [1, 4, 9, 16, 25]
```

### `filter()` — Keep Items Matching a Condition

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8]
```

### Combining `enumerate` and `zip`

```python
names  = ["Alice", "Bob"]
scores = [88, 95]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} scored {score}")
```

---

## 7. List Comprehensions

A list comprehension is a **concise, readable way to build a list** using a `for` loop inside square brackets. It is usually faster than an equivalent `for` loop.

### Basic Syntax

```python
new_list = [expression for item in iterable if condition]
#            ^output     ^loop                ^filter (optional)
```

### Examples

```python
# Squares of numbers 1-10
squares = [x**2 for x in range(1, 11)]
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filter — only even squares
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)   # [4, 16, 36, 64, 100]

# Strings — uppercase all words
words = ["hello", "world", "python"]
upper = [word.upper() for word in words]
print(upper)   # ['HELLO', 'WORLD', 'PYTHON']

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conditional expression inside comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)   # ['even', 'odd', 'even', 'odd', 'even', 'odd']
```

### Comprehension vs. For Loop

```python
# Traditional for loop
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x ** 2)

# Equivalent list comprehension — cleaner and faster
result = [x**2 for x in range(10) if x % 2 == 0]
```

> [!TIP]
> List comprehensions are faster than `for` loops with `.append()` because they are optimized at the bytecode level in CPython. Prefer them for simple transformations and filters.

---

## 8. Dictionary & Set Comprehensions

The same comprehension syntax works for dictionaries and sets.

### Dictionary Comprehension

```python
# Syntax
new_dict = {key_expr: value_expr for item in iterable if condition}

# Square each number as a key-value pair
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# Filter a dictionary
scores = {"Alice": 88, "Bob": 55, "Carol": 92, "Dan": 47}
passing = {name: score for name, score in scores.items() if score >= 60}
print(passing)   # {'Alice': 88, 'Carol': 92}
```

### Set Comprehension

```python
# Syntax — curly braces, no key:value pair
new_set = {expression for item in iterable if condition}

# Unique squares
unique_squares = {x**2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(unique_squares)   # {0, 1, 4, 9}  — duplicates removed automatically
```

### Generator Expression

Like a list comprehension but **lazy** — produces values one at a time without building the full list in memory.

```python
# List comprehension — builds entire list
squares_list = [x**2 for x in range(1_000_000)]    # uses ~8MB RAM

# Generator expression — lazy, uses almost no memory
squares_gen = (x**2 for x in range(1_000_000))     # uses ~200 bytes

# Use with sum(), max(), min() etc.
total = sum(x**2 for x in range(1000))
print(total)
```

---

## 9. Iterators & Iterables

Understanding the difference between an iterable and an iterator is key to mastering loops in Python.

| Concept | Definition | Example |
|---------|------------|---------|
| **Iterable** | Any object you can loop over | `list`, `str`, `dict`, `range` |
| **Iterator** | An object with state that knows the next value | result of `iter()`, generators |

```python
# Every for loop calls iter() on the iterable internally
fruits = ["apple", "banana", "mango"]

# What Python actually does under the hood
iterator = iter(fruits)
print(next(iterator))   # apple
print(next(iterator))   # banana
print(next(iterator))   # mango
# next(iterator) now raises StopIteration — loop ends

# Manual iteration
numbers = [10, 20, 30]
it = iter(numbers)
while True:
    try:
        val = next(it)
        print(val)
    except StopIteration:
        break
```

### Building a Custom Iterator

```python
class CountUp:
    """Iterator that counts from start to stop."""

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


for num in CountUp(1, 6):
    print(num)   # 1 2 3 4 5
```

---

## 10. The `else` Clause on Loops

Python loops support an `else` block — one of the most underused features in the language. The `else` block runs **only if the loop completed without hitting a `break`**.

```python
# else on a for loop
for i in range(5):
    if i == 10:   # never true
        break
else:
    print("Loop finished without break")   # this runs

# else on a while loop
count = 0
while count < 3:
    count += 1
else:
    print("While loop completed normally")   # this runs
```

### Real-World Use: Search with `else`

```python
# Find a prime number — classic use case
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is divisible by {i}")
            break
    else:
        # Only reaches here if no divisor was found
        print(f"{n} is prime")
        return True
    return False

is_prime(7)    # 7 is prime
is_prime(12)   # 12 is divisible by 2
```

### Search in a List

```python
users = ["Alice", "Bob", "Charlie"]
target = "Dave"

for user in users:
    if user == target:
        print(f"Found: {user}")
        break
else:
    print(f"{target} not found in the list")
# Output: Dave not found in the list
```

> [!TIP]
> Think of the loop `else` as "no break" — it runs when the loop exhausted all items without breaking out. This is cleaner than using a flag variable like `found = False`.

---

## 11. Performance & Best Practices

### Prefer `for` over `while` when possible

```python
# Less Pythonic
i = 0
while i < len(items):
    print(items[i])
    i += 1

# More Pythonic
for item in items:
    print(item)
```

### Never Modify a List While Iterating It

```python
numbers = [1, 2, 3, 4, 5]

# BAD — skips elements silently
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

# GOOD — iterate over a copy
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)

# BEST — use a comprehension
numbers = [num for num in numbers if num % 2 != 0]
```

### Use `enumerate()` Instead of `range(len())`

```python
items = ["a", "b", "c"]

# Bad — old school style
for i in range(len(items)):
    print(i, items[i])

# Good — clean and Pythonic
for i, item in enumerate(items):
    print(i, item)
```

### Avoid Unnecessary Work Inside Loops

```python
data = [1, 2, 3, 4, 5]

# Bad — len() is called on every iteration (minor, but a bad habit)
for i in range(len(data)):
    print(data[i])

# Good — compute once, use many
n = len(data)
for i in range(n):
    print(data[i])

# Best — just iterate directly
for item in data:
    print(item)
```

### Use `any()` and `all()` Instead of Manual Loops

```python
numbers = [2, 4, 6, 8, 10]

# Bad
all_even = True
for n in numbers:
    if n % 2 != 0:
        all_even = False
        break

# Good — clean and expressive
all_even = all(n % 2 == 0 for n in numbers)
has_even = any(n % 2 == 0 for n in numbers)
```

### Performance Comparison

| Approach | Speed | Memory | Use Case |
|----------|-------|--------|----------|
| `for` loop + `append` | Moderate | High | Simple iteration |
| List comprehension | Fast | High | Transform/filter a list |
| Generator expression | Fast | Very Low | Large datasets, one-time use |
| `map()` / `filter()` | Fast | Low | Functional style transformations |
| `while` loop | Varies | Low | Unknown iteration count |
| `numpy` vectorized | Very Fast | Medium | Numerical computation |

> [!WARNING]
> Avoid bare `while True` loops without a guaranteed exit condition (`break` or a condition that will eventually turn `False`). They are the most common source of frozen programs.

---

## 12. Quick Reference Cheat Sheet

```python
# ── FOR LOOP ──────────────────────────────────────
for item in iterable:           # basic
for i in range(n):              # counted
for i in range(start, stop):    # range with start
for i in range(start, stop, step): # with step
for i, v in enumerate(lst):     # with index
for a, b in zip(lst1, lst2):    # two lists together
for k, v in dict.items():       # dict key-value

# ── WHILE LOOP ────────────────────────────────────
while condition:                # basic
while True:                     # loop forever (needs break)

# ── CONTROL ───────────────────────────────────────
break                           # exit loop immediately
continue                        # skip to next iteration
pass                            # do nothing, placeholder

# ── ELSE CLAUSE ───────────────────────────────────
for ...:
    ...
else:
    # runs if no break occurred

# ── COMPREHENSIONS ────────────────────────────────
[expr for x in iterable]                    # list
[expr for x in iterable if condition]       # filtered list
{k: v for k, v in iterable}                # dict
{expr for x in iterable}                   # set
(expr for x in iterable)                   # generator

# ── USEFUL BUILT-INS IN LOOPS ─────────────────────
enumerate(iterable, start=0)    # index + value
zip(iter1, iter2)               # parallel iteration
reversed(iterable)              # iterate backwards
sorted(iterable, reverse=False) # iterate sorted
map(func, iterable)             # apply function to each
filter(func, iterable)          # keep matching items
any(condition for x in iter)    # True if any match
all(condition for x in iter)    # True if all match
```

---

## When to Use What

| Situation | Best Choice |
|-----------|-------------|
| Iterating over a list, string, dict | `for` loop |
| Counting from 0 to N | `for i in range(n)` |
| Need index while iterating | `enumerate()` |
| Iterating two lists in parallel | `zip()` |
| Don't know the count upfront | `while` loop |
| Validate user input | `while True` + `break` |
| Build a new list from an existing one | List comprehension |
| Filter a list | List comprehension with `if` |
| Large data, memory-sensitive | Generator expression |
| Search and detect if not found | `for` + `else` |
| Apply function to every element | `map()` or comprehension |
| Check if any/all items match | `any()` / `all()` |

---

<div align="center">

**Python Loops Reference** — Made with 💚 by Haseeb

*Python 3.10+ · Feel free to fork and star ⭐*

</div>
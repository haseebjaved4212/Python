# 📋 Python Lists — Complete Reference

> A thorough, practical guide to Python lists — from creating and accessing to slicing, sorting, and advanced patterns used in real-world code.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-13-orange?style=flat-square)
![Examples](https://img.shields.io/badge/Code%20Examples-50+-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

---

## 📚 Table of Contents

1. [What is a List?](#1-what-is-a-list)
2. [Creating Lists](#2-creating-lists)
3. [Accessing Elements](#3-accessing-elements)
4. [Slicing](#4-slicing)
5. [Modifying Lists](#5-modifying-lists)
6. [List Methods](#6-list-methods)
7. [Iterating Over Lists](#7-iterating-over-lists)
8. [List Comprehensions](#8-list-comprehensions)
9. [Sorting & Ordering](#9-sorting--ordering)
10. [Copying Lists](#10-copying-lists)
11. [Nested Lists](#11-nested-lists)
12. [Lists vs Other Data Structures](#12-lists-vs-other-data-structures)
13. [Best Practices & Performance](#13-best-practices--performance)

---

## 1. What is a List?

A list is Python's most versatile, widely used **built-in data structure**. It is an **ordered, mutable, indexed** collection that can hold any mix of data types — integers, strings, booleans, objects, even other lists.

```python
# A list can hold anything
mixed = [42, "hello", 3.14, True, None, [1, 2, 3]]
```

### Core Characteristics

| Property | Description |
|----------|-------------|
| **Ordered** | Items maintain their insertion order |
| **Mutable** | You can add, remove, or change items after creation |
| **Indexed** | Each item has a position starting from `0` |
| **Allows duplicates** | Same value can appear multiple times |
| **Mixed types** | Can hold any combination of data types |
| **Dynamic size** | Grows and shrinks as needed at runtime |

### Why Lists?

```python
# Without a list — unscalable
student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"

# With a list — clean, scalable, powerful
students = ["Alice", "Bob", "Charlie"]
```

---

## 2. Creating Lists

Python gives you several ways to create a list depending on your use case.

### Literal Syntax

```python
# Empty list
empty = []

# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
colors = ["red", "green", "blue"]

# Mixed types
profile = ["Haseeb", 25, True, 3.14]

# List with duplicate values
scores = [90, 85, 90, 70, 85]
```

### Using `list()` Constructor

```python
# From a string — each character becomes an item
chars = list("Python")
print(chars)   # ['P', 'y', 't', 'h', 'o', 'n']

# From a tuple
nums = list((1, 2, 3, 4))
print(nums)    # [1, 2, 3, 4]

# From a range
evens = list(range(0, 11, 2))
print(evens)   # [0, 2, 4, 6, 8, 10]

# From a set (order not guaranteed)
unique = list({3, 1, 4, 1, 5, 9})
print(unique)  # [1, 3, 4, 5, 9]  — order varies
```

### Using List Comprehension

```python
# Squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Using `*` Repetition Operator

```python
# Create a list with repeated values
zeros     = [0] * 5
print(zeros)      # [0, 0, 0, 0, 0]

placeholders = [None] * 3
print(placeholders)  # [None, None, None]
```

> [!WARNING]
> Be careful using `*` with mutable objects. `[[]] * 3` creates three references to the **same** inner list, not three independent lists. Use a comprehension instead.

```python
# BAD — all three rows are the same object in memory
grid_bad = [[0] * 3] * 3
grid_bad[0][0] = 9
print(grid_bad)   # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]  ← unexpected!

# GOOD — each row is independent
grid_good = [[0] * 3 for _ in range(3)]
grid_good[0][0] = 9
print(grid_good)  # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]  ← correct
```

---

## 3. Accessing Elements

Lists are **zero-indexed** — the first element is at position `0`.

### Positive Indexing

```python
fruits = ["apple", "banana", "mango", "orange", "grape"]
#          [0]       [1]       [2]      [3]       [4]

print(fruits[0])   # apple
print(fruits[2])   # mango
print(fruits[4])   # grape
```

### Negative Indexing

Negative indices count from the **end** of the list.

```python
fruits = ["apple", "banana", "mango", "orange", "grape"]
#          [-5]      [-4]      [-3]     [-2]      [-1]

print(fruits[-1])   # grape   — last item
print(fruits[-2])   # orange  — second to last
print(fruits[-5])   # apple   — same as fruits[0]
```

### Index Reference Table

```
 List:   ["apple", "banana", "mango", "orange", "grape"]
 Pos:       [0]      [1]      [2]      [3]      [4]
 Neg:       [-5]     [-4]     [-3]     [-2]     [-1]
```

### Accessing Nested List Items

```python
data = [10, [20, 30, [40, 50]], 60]

print(data[1])         # [20, 30, [40, 50]]
print(data[1][0])      # 20
print(data[1][2])      # [40, 50]
print(data[1][2][1])   # 50
```

> [!WARNING]
> Accessing an index that does not exist raises an `IndexError`. Always check length or use `try/except` when the index might be out of range.

```python
items = [1, 2, 3]
print(items[5])   # IndexError: list index out of range

# Safe access
index = 5
value = items[index] if index < len(items) else "Not found"
```

---

## 4. Slicing

Slicing extracts a **portion** of a list and returns a new list. The original is not modified.

### Syntax

```python
list[start : stop : step]
#    inclusive  exclusive  optional
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `start` | Index to begin from (inclusive) | `0` |
| `stop` | Index to end at (exclusive) | `len(list)` |
| `step` | How many to skip between items | `1` |

### Basic Slicing

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])    # [2, 3, 4, 5]       — index 2 up to (not including) 6
print(nums[:4])     # [0, 1, 2, 3]       — from beginning to index 4
print(nums[6:])     # [6, 7, 8, 9]       — from index 6 to end
print(nums[:])      # [0, 1, 2, ..., 9]  — full copy
```

### Slicing with Step

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[::2])     # [0, 2, 4, 6, 8]   — every 2nd item
print(nums[1::2])    # [1, 3, 5, 7, 9]   — every 2nd item starting at 1
print(nums[::3])     # [0, 3, 6, 9]      — every 3rd item
```

### Negative Step — Reversing

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  — reversed
print(nums[7:2:-1])  # [7, 6, 5, 4, 3]  — from index 7 down to (not including) 2
```

### Common Slice Patterns

```python
items = [10, 20, 30, 40, 50, 60, 70, 80]

first_three  = items[:3]         # [10, 20, 30]
last_three   = items[-3:]        # [60, 70, 80]
without_first = items[1:]        # [20, 30, 40, 50, 60, 70, 80]
without_last  = items[:-1]       # [10, 20, 30, 40, 50, 60, 70]
middle        = items[2:-2]      # [30, 40, 50, 60]
reversed_list = items[::-1]      # [80, 70, 60, 50, 40, 30, 20, 10]
shallow_copy  = items[:]         # [10, 20, 30, 40, 50, 60, 70, 80]
```

---

## 5. Modifying Lists

Since lists are **mutable**, you can change them after creation.

### Changing a Single Item

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'mango']
```

### Changing Multiple Items via Slice Assignment

```python
nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30, 40]
print(nums)   # [1, 20, 30, 40, 5]

# Replace a slice with more or fewer items
nums[1:3] = [200, 300, 400, 500]
print(nums)   # [1, 200, 300, 400, 500, 40, 5]
```

### Adding Items

```python
fruits = ["apple", "banana"]

# Add to the end
fruits.append("mango")
print(fruits)   # ['apple', 'banana', 'mango']

# Insert at a specific index
fruits.insert(1, "blueberry")
print(fruits)   # ['apple', 'blueberry', 'banana', 'mango']

# Add all items from another iterable
fruits.extend(["grape", "kiwi"])
print(fruits)   # ['apple', 'blueberry', 'banana', 'mango', 'grape', 'kiwi']

# Concatenation — creates a new list
more = fruits + ["pear", "melon"]
```

### Removing Items

```python
items = [10, 20, 30, 40, 50, 30]

# Remove by value — removes FIRST occurrence only
items.remove(30)
print(items)   # [10, 20, 40, 50, 30]

# Remove by index — returns the removed item
popped = items.pop(1)
print(popped)  # 20
print(items)   # [10, 40, 50, 30]

# Remove last item (default pop)
last = items.pop()
print(last)    # 30

# Remove by index without returning
del items[0]
print(items)   # [40, 50]

# Clear all items
items.clear()
print(items)   # []
```

> [!NOTE]
> `remove()` raises a `ValueError` if the value is not in the list. Always check with `in` first or wrap in `try/except`.

```python
items = [1, 2, 3]

# Safe remove
value = 99
if value in items:
    items.remove(value)
else:
    print(f"{value} not in list")
```

---

## 6. List Methods

Python lists come with a rich set of built-in methods. Here is every one of them.

### Complete Methods Reference

| Method | Syntax | Description | Returns |
|--------|--------|-------------|---------|
| `append()` | `lst.append(x)` | Add item to the end | `None` |
| `insert()` | `lst.insert(i, x)` | Insert item at index `i` | `None` |
| `extend()` | `lst.extend(iter)` | Add all items from iterable | `None` |
| `remove()` | `lst.remove(x)` | Remove first occurrence of `x` | `None` |
| `pop()` | `lst.pop(i=-1)` | Remove and return item at index | item |
| `clear()` | `lst.clear()` | Remove all items | `None` |
| `index()` | `lst.index(x)` | Return index of first `x` | `int` |
| `count()` | `lst.count(x)` | Count occurrences of `x` | `int` |
| `sort()` | `lst.sort()` | Sort in place | `None` |
| `reverse()` | `lst.reverse()` | Reverse in place | `None` |
| `copy()` | `lst.copy()` | Return a shallow copy | `list` |

### Code Examples for Every Method

```python
items = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# append
items.append(3)
print(items)          # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# insert
items.insert(2, 99)
print(items)          # [3, 1, 99, 4, 1, 5, 9, 2, 6, 5, 3]

# extend
items.extend([7, 8])
print(items)          # [..., 7, 8]

# remove — removes first 1
items.remove(1)

# pop — removes and returns last item
last = items.pop()

# pop at index
third = items.pop(2)

# index — find first occurrence
print(items.index(5))  # position of first 5

# count
print(items.count(5))  # how many times 5 appears

# sort
nums = [5, 2, 8, 1, 9]
nums.sort()
print(nums)            # [1, 2, 5, 8, 9]

nums.sort(reverse=True)
print(nums)            # [9, 8, 5, 2, 1]

# reverse
nums.reverse()
print(nums)            # [1, 2, 5, 8, 9]

# copy
original = [1, 2, 3]
clone = original.copy()
```

### `append()` vs `extend()` vs `+`

```python
base = [1, 2, 3]

# append — adds the object as a single item
a = base.copy()
a.append([4, 5])
print(a)   # [1, 2, 3, [4, 5]]   ← nested list

# extend — unpacks the iterable and adds each item
b = base.copy()
b.extend([4, 5])
print(b)   # [1, 2, 3, 4, 5]    ← flat

# + — creates a brand new list
c = base + [4, 5]
print(c)   # [1, 2, 3, 4, 5]    ← new list, base unchanged
```

---

## 7. Iterating Over Lists

### Basic `for` Loop

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
```

### With Index using `enumerate()`

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start index at 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

### Iterating Two Lists in Parallel with `zip()`

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

### `while` Loop with Index

```python
items = [10, 20, 30, 40]
i = 0
while i < len(items):
    print(items[i])
    i += 1
```

### Iterating in Reverse

```python
items = [1, 2, 3, 4, 5]

for item in reversed(items):
    print(item)   # 5 4 3 2 1

# Or using slicing
for item in items[::-1]:
    print(item)
```

> [!WARNING]
> Never add or remove items from a list while iterating over it with a `for` loop. It causes skipped elements or an infinite loop. Iterate over a copy or use a comprehension instead.

```python
numbers = [1, 2, 3, 4, 5, 6]

# BAD — modifying while iterating
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

# GOOD — iterate a copy, modify original
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)

# BEST — build a new list
numbers = [n for n in numbers if n % 2 != 0]
```

---

## 8. List Comprehensions

A list comprehension is a concise, readable, and faster way to build a new list from an existing iterable.

### Syntax

```python
new_list = [expression for item in iterable if condition]
#            ^output      ^loop               ^filter (optional)
```

### Examples

```python
# All squares 1-10
squares = [x**2 for x in range(1, 11)]

# Filter — only even numbers
evens = [x for x in range(20) if x % 2 == 0]

# Transform strings
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]

# Conditional expression inside
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
# ['even', 'odd', 'even', 'odd', 'even', 'odd']

# Nested comprehension — flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Apply a function to each item
import math
roots = [round(math.sqrt(x), 2) for x in [4, 9, 16, 25, 36]]
# [2.0, 3.0, 4.0, 5.0, 6.0]

# Filter objects by attribute
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob",   "grade": 55},
    {"name": "Carol", "grade": 92},
]
passing = [s["name"] for s in students if s["grade"] >= 60]
# ['Alice', 'Carol']
```

### Comprehension vs Traditional Loop

```python
# Traditional — verbose
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x ** 2)

# Comprehension — clean, fast, Pythonic
result = [x**2 for x in range(10) if x % 2 == 0]
```

> [!TIP]
> List comprehensions are faster than a `for` loop with `.append()` because they are optimized at the CPython bytecode level. Prefer them for simple transformations. For very complex logic, a regular loop is more readable.

---

## 9. Sorting & Ordering

Python gives you two ways to sort: **in-place** with `.sort()` and **returning a new list** with `sorted()`.

### `.sort()` — Modifies in Place

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.sort()
print(nums)   # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True)
print(nums)   # [9, 6, 5, 4, 3, 2, 1, 1]
```

### `sorted()` — Returns a New List

```python
original = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(original)

print(original)     # [3, 1, 4, 1, 5, 9]  — unchanged
print(sorted_nums)  # [1, 1, 3, 4, 5, 9]
```

### Sort by Custom Key

```python
words = ["banana", "apple", "kiwi", "strawberry", "fig"]

# Sort by string length
words.sort(key=len)
print(words)   # ['fig', 'kiwi', 'apple', 'banana', 'strawberry']

# Sort alphabetically (case-insensitive)
words.sort(key=str.lower)

# Sort a list of dicts by a field
students = [
    {"name": "Charlie", "gpa": 3.5},
    {"name": "Alice",   "gpa": 3.9},
    {"name": "Bob",     "gpa": 3.2},
]

students.sort(key=lambda s: s["gpa"], reverse=True)
for s in students:
    print(s["name"], s["gpa"])
# Alice 3.9
# Charlie 3.5
# Bob 3.2
```

### Sort by Multiple Keys

```python
data = [
    ("Alice", 25, 88),
    ("Bob",   25, 95),
    ("Carol", 22, 88),
]

# Sort by age first, then by score descending
data.sort(key=lambda x: (x[1], -x[2]))
```

### `.sort()` vs `sorted()` Comparison

| Feature | `.sort()` | `sorted()` |
|---------|-----------|------------|
| Modifies original | Yes | No |
| Returns | `None` | New list |
| Works on | Lists only | Any iterable |
| Memory | More efficient | Creates new list |
| Use when | You don't need the original | You need both lists |

---

## 10. Copying Lists

Copying lists in Python has a common trap — knowing when you get a new list vs. a reference to the same one.

### Assignment is NOT a Copy

```python
original = [1, 2, 3]
alias = original   # both point to the SAME list

alias.append(99)
print(original)    # [1, 2, 3, 99]  ← original changed!
```

### Shallow Copy — Four Ways

```python
original = [1, 2, 3, 4, 5]

copy1 = original.copy()       # built-in method
copy2 = original[:]           # slice syntax
copy3 = list(original)        # list constructor
copy4 = [x for x in original] # comprehension

copy1.append(99)
print(original)   # [1, 2, 3, 4, 5]  — untouched
```

### Shallow vs Deep Copy

A shallow copy creates a new list but inner objects are still shared references.

```python
import copy

nested = [[1, 2], [3, 4], [5, 6]]

shallow = nested.copy()
deep    = copy.deepcopy(nested)

# Modify inner list
nested[0][0] = 99

print(shallow)  # [[99, 2], [3, 4], [5, 6]]  ← affected!
print(deep)     # [[1, 2], [3, 4], [5, 6]]   ← safe
```

> [!TIP]
> Use `copy.deepcopy()` whenever your list contains mutable objects like other lists, dicts, or custom class instances and you need a fully independent copy.

---

## 11. Nested Lists

A nested list (also called a 2D list or matrix) is a list where each element is itself a list.

### Creating a Matrix

```python
# 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 1, column 2
print(matrix[1][2])   # 6

# Access full row
print(matrix[0])      # [1, 2, 3]
```

### Iterating a 2D List

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### Modifying a Matrix

```python
matrix = [[0] * 3 for _ in range(3)]

# Set diagonal to 1
for i in range(3):
    matrix[i][i] = 1

print(matrix)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
```

### Transpose a Matrix

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using zip
transposed = [list(row) for row in zip(*matrix)]
print(transposed)
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
```

---

## 12. Lists vs Other Data Structures

Knowing when to use a list vs another structure is a key engineering skill.

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Ordered | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes (3.7+) |
| Mutable | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Indexed | ✅ Yes | ✅ Yes | ❌ No | ✅ By key |
| Duplicates | ✅ Yes | ✅ Yes | ❌ No | ❌ No (keys) |
| Syntax | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"k": "v"}` |
| Use for | General sequences | Fixed data | Unique items | Key-value pairs |

### When to Use Each

```python
# List — ordered, changeable sequence
shopping_cart = ["apple", "milk", "bread"]

# Tuple — fixed data that should not change
rgb_color = (255, 128, 0)
coordinates = (40.7128, -74.0060)

# Set — unique items, fast membership check
unique_visitors = {"alice", "bob", "charlie"}
if "alice" in unique_visitors:   # O(1) lookup
    print("Alice visited")

# Dict — fast lookup by key
user = {"name": "Haseeb", "age": 25, "role": "dev"}
print(user["name"])   # Haseeb
```

### List vs `collections.deque` for Queue Operations

```python
from collections import deque

# List as a queue — O(n) for pop(0), slow for large lists
queue_list = [1, 2, 3]
queue_list.pop(0)       # O(n) — shifts all elements

# deque — O(1) for both ends, use for queues
queue_deque = deque([1, 2, 3])
queue_deque.popleft()   # O(1) — efficient
```

> [!TIP]
> If you are frequently adding/removing from the **beginning** of a sequence, use `collections.deque` instead of a list. If you need fast lookups by value, use a `set` or `dict`.

---

## 13. Best Practices & Performance

### Use Comprehensions Over Manual Loops

```python
# Slow
result = []
for x in range(1000):
    result.append(x * 2)

# Fast and Pythonic
result = [x * 2 for x in range(1000)]
```

### Preallocate When Size is Known

```python
# Growing a list one by one — multiple reallocations
result = []
for i in range(10000):
    result.append(i)

# Better — preallocate with a comprehension
result = [i for i in range(10000)]

# Or simply
result = list(range(10000))
```

### Membership Testing

```python
items = [1, 2, 3, 4, 5]

# List — O(n) linear scan, slow for large lists
if 3 in items: ...

# Set — O(1) hash lookup, fast for large collections
items_set = set(items)
if 3 in items_set: ...
```

### Use `any()` and `all()` Instead of Manual Loops

```python
scores = [72, 85, 90, 61, 95]

# Manual — verbose
all_passing = True
for s in scores:
    if s < 60:
        all_passing = False
        break

# Pythonic
all_passing = all(s >= 60 for s in scores)
any_failing  = any(s < 60 for s in scores)
```

### Unpack Lists Cleanly

```python
point = [10, 20, 30]
x, y, z = point
print(x, y, z)   # 10 20 30

# Extended unpacking
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*beginning, last = [1, 2, 3, 4, 5]
print(beginning)  # [1, 2, 3, 4]
print(last)       # 5
```

### Common Pitfalls to Avoid

```python
# 1. Using a list as a function default argument
def bad(items=[]):         # shared across calls!
    items.append(1)
    return items

def good(items=None):      # correct
    if items is None:
        items = []
    items.append(1)
    return items

# 2. Modifying while iterating
# Use a copy or comprehension — see Section 7

# 3. Using + in a loop to concatenate
result = []
for i in range(1000):
    result = result + [i]   # creates a new list every iteration — O(n²)!

# Use extend or append instead
result = []
for i in range(1000):
    result.append(i)        # O(1) amortized
```

### Performance Cheat Sheet

| Operation | Time Complexity |
|-----------|----------------|
| `list[i]` — index access | O(1) |
| `list.append(x)` | O(1) amortized |
| `list.pop()` — remove last | O(1) |
| `list.pop(0)` — remove first | O(n) |
| `list.insert(i, x)` | O(n) |
| `x in list` — membership | O(n) |
| `list.sort()` | O(n log n) |
| `list[a:b]` — slicing | O(b - a) |
| `len(list)` | O(1) |

---

## Quick Reference Cheat Sheet

```python
# ── CREATING ─────────────────────────────────────────
lst = []                         # empty
lst = [1, 2, 3]                  # literal
lst = list(range(10))            # from range
lst = list("abc")                # from string → ['a','b','c']
lst = [x**2 for x in range(5)]   # comprehension

# ── ACCESSING ─────────────────────────────────────────
lst[0]          # first item
lst[-1]         # last item
lst[i]          # item at index i

# ── SLICING ───────────────────────────────────────────
lst[a:b]        # items from a to b (exclusive)
lst[a:b:step]   # with step
lst[::-1]       # reversed
lst[:]          # shallow copy

# ── MODIFYING ─────────────────────────────────────────
lst.append(x)        # add to end
lst.insert(i, x)     # insert at index
lst.extend(iter)     # add all from iterable
lst[i] = x           # change item at index
lst[a:b] = [...]     # replace slice

# ── REMOVING ──────────────────────────────────────────
lst.remove(x)    # remove first occurrence of x
lst.pop(i)       # remove and return item at i
lst.pop()        # remove and return last item
del lst[i]       # delete item at index
lst.clear()      # remove all items

# ── SEARCHING ─────────────────────────────────────────
x in lst         # True if x exists
lst.index(x)     # index of first x
lst.count(x)     # how many times x appears

# ── SORTING ───────────────────────────────────────────
lst.sort()                     # sort in place
lst.sort(reverse=True)         # descending
lst.sort(key=func)             # by custom key
sorted(lst)                    # new sorted list

# ── COPYING ───────────────────────────────────────────
lst.copy()          # shallow copy
lst[:]              # shallow copy via slice
copy.deepcopy(lst)  # deep copy (nested safe)

# ── USEFUL BUILT-INS ──────────────────────────────────
len(lst)            # number of items
min(lst)            # smallest item
max(lst)            # largest item
sum(lst)            # sum of all items
reversed(lst)       # iterator in reverse
enumerate(lst)      # (index, item) pairs
zip(lst1, lst2)     # parallel iteration
any(cond for x in lst)   # True if any match
all(cond for x in lst)   # True if all match
```

---

<div align="center">

**Python Lists Reference** — Made with 💚 by Haseeb

*Python 3.10+ · Feel free to fork and star ⭐*

</div>
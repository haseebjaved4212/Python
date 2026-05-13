# 🔷 Python Tuples — Complete Reference

> A thorough, practical guide to Python tuples — from creation and indexing to unpacking, named tuples, and when to choose a tuple over a list.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-13-orange?style=flat-square)
![Examples](https://img.shields.io/badge/Code%20Examples-50+-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

---

## 📚 Table of Contents

1. [What is a Tuple?](#1-what-is-a-tuple)
2. [Creating Tuples](#2-creating-tuples)
3. [Accessing Elements](#3-accessing-elements)
4. [Slicing Tuples](#4-slicing-tuples)
5. [Tuple Immutability](#5-tuple-immutability)
6. [Tuple Methods](#6-tuple-methods)
7. [Tuple Packing & Unpacking](#7-tuple-packing--unpacking)
8. [Iterating Over Tuples](#8-iterating-over-tuples)
9. [Tuples as Dictionary Keys](#9-tuples-as-dictionary-keys)
10. [Named Tuples](#10-named-tuples)
11. [Tuples vs Lists](#11-tuples-vs-lists)
12. [Performance & Memory](#12-performance--memory)
13. [Best Practices & Real-World Patterns](#13-best-practices--real-world-patterns)

---

## 1. What is a Tuple?

A tuple is Python's **immutable, ordered** sequence type. Think of it as a list that cannot be changed after creation — no adding, no removing, no replacing items. That constraint is not a limitation — it is a feature that makes tuples faster, safer, and more expressive than lists for the right jobs.

```python
# A tuple — defined with parentheses
point     = (10, 20)
rgb       = (255, 128, 0)
person    = ("Haseeb", 25, "Karachi")
mixed     = (1, "hello", 3.14, True, None)
```

### Core Characteristics

| Property | Description |
|----------|-------------|
| **Ordered** | Items maintain their insertion order |
| **Immutable** | Cannot be changed after creation |
| **Indexed** | Each item has a position starting from `0` |
| **Allows duplicates** | Same value can appear multiple times |
| **Hashable** | Can be used as dictionary keys or set members (if all items are hashable) |
| **Mixed types** | Can hold any combination of data types |
| **Faster than lists** | Lower memory overhead and faster iteration |

### The Core Idea

```python
# Use a list when data can change
shopping_cart = ["apple", "milk", "bread"]
shopping_cart.append("eggs")   # makes sense — cart changes

# Use a tuple when data is fixed by nature
coordinates  = (40.7128, -74.0060)   # latitude, longitude never change
rgb_red      = (255, 0, 0)           # color values are fixed
http_methods = ("GET", "POST", "PUT", "DELETE")
```

---

## 2. Creating Tuples

### Literal Syntax

```python
# Empty tuple
empty = ()

# Single item tuple — the trailing comma is REQUIRED
single = (42,)
also_single = 42,        # parentheses are optional
not_a_tuple = (42)       # this is just the integer 42, not a tuple!

print(type(single))      # <class 'tuple'>
print(type(not_a_tuple)) # <class 'int'>

# Multiple items
numbers  = (1, 2, 3, 4, 5)
colors   = ("red", "green", "blue")
mixed    = ("Haseeb", 25, True, 3.14)
```

> [!WARNING]
> The single-item tuple gotcha catches almost every Python developer at some point. `(42)` is just `42` wrapped in parentheses — the math kind, not a tuple. Always add a trailing comma: `(42,)`.

### Using `tuple()` Constructor

```python
# From a list
from_list = tuple([1, 2, 3, 4])
print(from_list)     # (1, 2, 3, 4)

# From a string
from_str = tuple("Python")
print(from_str)      # ('P', 'y', 't', 'h', 'o', 'n')

# From a range
from_range = tuple(range(1, 6))
print(from_range)    # (1, 2, 3, 4, 5)

# From a set (order not guaranteed)
from_set = tuple({3, 1, 4, 1, 5})
print(from_set)      # some order of (1, 3, 4, 5)

# From a dict (gives keys only)
from_dict = tuple({"a": 1, "b": 2, "c": 3})
print(from_dict)     # ('a', 'b', 'c')
```

### Tuple Packing — No Parentheses Needed

Python lets you create a tuple by just separating values with commas. The parentheses are syntactic sugar, not a requirement.

```python
# These are all the same
coords   = (10, 20, 30)
coords   = 10, 20, 30    # tuple packing without parentheses

# Useful for returning multiple values from a function
def get_user():
    return "Haseeb", 25, "Karachi"   # returns a tuple

name, age, city = get_user()
```

### Nested Tuples

```python
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Mix of types
record = ("Haseeb", (25, "Karachi"), ("Python", "React"))
```

---

## 3. Accessing Elements

Tuples are zero-indexed — the same as lists.

### Positive Indexing

```python
fruits = ("apple", "banana", "mango", "orange", "grape")
#          [0]       [1]       [2]      [3]       [4]

print(fruits[0])   # apple
print(fruits[2])   # mango
print(fruits[4])   # grape
```

### Negative Indexing

```python
fruits = ("apple", "banana", "mango", "orange", "grape")
#          [-5]      [-4]      [-3]     [-2]      [-1]

print(fruits[-1])  # grape  — last item
print(fruits[-2])  # orange — second to last
print(fruits[-5])  # apple  — same as fruits[0]
```

### Index Reference Map

```
Tuple:    ("apple", "banana", "mango", "orange", "grape")
Positive:   [0]      [1]       [2]      [3]       [4]
Negative:   [-5]     [-4]      [-3]     [-2]      [-1]
```

### Accessing Nested Tuple Elements

```python
record = ("Haseeb", (25, "Karachi"), ("Python", "React", "TypeScript"))

print(record[0])          # Haseeb
print(record[1])          # (25, 'Karachi')
print(record[1][0])       # 25
print(record[1][1])       # Karachi
print(record[2][2])       # TypeScript
```

> [!WARNING]
> Accessing an index out of range raises `IndexError`. Tuples have no `.get()` method like dicts — use `try/except` or check `len()` first.

```python
data = (10, 20, 30)

# Safe access
index = 5
value = data[index] if index < len(data) else "Index out of range"
print(value)   # Index out of range
```

---

## 4. Slicing Tuples

Slicing a tuple returns a **new tuple** — the original is untouched (and unchanged regardless since tuples are immutable).

### Syntax

```python
tuple[start : stop : step]
#     inclusive  exclusive  optional
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `start` | Index to begin from (inclusive) | `0` |
| `stop` | Index to end at (exclusive) | `len(tuple)` |
| `step` | How many to skip between items | `1` |

### Examples

```python
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(nums[2:6])     # (2, 3, 4, 5)
print(nums[:4])      # (0, 1, 2, 3)
print(nums[6:])      # (6, 7, 8, 9)
print(nums[:])       # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(nums[::2])     # (0, 2, 4, 6, 8)   — every 2nd item
print(nums[::-1])    # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)  — reversed
print(nums[7:2:-1])  # (7, 6, 5, 4, 3)
```

### Common Slice Patterns

```python
items = (10, 20, 30, 40, 50, 60, 70, 80)

first_three   = items[:3]     # (10, 20, 30)
last_three    = items[-3:]    # (60, 70, 80)
without_first = items[1:]     # (20, 30, 40, 50, 60, 70, 80)
without_last  = items[:-1]    # (10, 20, 30, 40, 50, 60, 70)
middle        = items[2:-2]   # (30, 40, 50, 60)
reversed_t    = items[::-1]   # (80, 70, 60, 50, 40, 30, 20, 10)
```

---

## 5. Tuple Immutability

Immutability is the defining feature of tuples. Once created, the tuple structure cannot change.

### What Immutability Means

```python
point = (10, 20, 30)

# These all raise TypeError
point[0] = 99        # TypeError: 'tuple' object does not support item assignment
point.append(40)     # AttributeError: 'tuple' object has no attribute 'append'
del point[0]         # TypeError: 'tuple' object doesn't support item deletion
```

### Immutability is Shallow

A tuple cannot be reassigned at the tuple level, but if it holds a mutable object (like a list), that inner object can still be mutated.

```python
# Tuple containing a list
data = (1, 2, [3, 4, 5])

# Changing the tuple structure fails
data[0] = 99          # TypeError!

# But changing the inner list works
data[2].append(6)
data[2][0] = 99
print(data)           # (1, 2, [99, 4, 5, 6])
```

> [!WARNING]
> If you store mutable objects inside a tuple, the tuple is no longer truly immutable in behavior. Avoid putting lists inside tuples when you intend the data to be fully fixed.

### "Modifying" a Tuple — Workarounds

Since tuples cannot be changed, the standard approach is to convert to a list, make changes, and convert back.

```python
original = (1, 2, 3, 4, 5)

# Convert, modify, convert back
temp = list(original)
temp[2] = 99
temp.append(6)
updated = tuple(temp)

print(original)  # (1, 2, 3, 4, 5)  — untouched
print(updated)   # (1, 2, 99, 4, 5, 6)
```

### Concatenation and Repetition

These do not modify the original — they create a new tuple.

```python
a = (1, 2, 3)
b = (4, 5, 6)

combined   = a + b        # (1, 2, 3, 4, 5, 6)  — new tuple
repeated   = a * 3        # (1, 2, 3, 1, 2, 3, 1, 2, 3)  — new tuple

print(a)    # (1, 2, 3)   — unchanged
```

---

## 6. Tuple Methods

Because tuples are immutable, they only have **two built-in methods** — they do not need the add/remove/sort methods that lists have.

### `.count(x)` — Count Occurrences

```python
scores = (90, 85, 90, 72, 90, 85, 61)

print(scores.count(90))   # 3
print(scores.count(85))   # 2
print(scores.count(100))  # 0  — no error, just returns 0
```

### `.index(x)` — Find First Occurrence

```python
fruits = ("apple", "banana", "mango", "banana", "orange")

print(fruits.index("banana"))        # 1  — first occurrence
print(fruits.index("mango"))         # 2

# Optional start and end parameters
print(fruits.index("banana", 2))     # 3  — search from index 2 onwards
print(fruits.index("banana", 2, 5))  # 3  — search between index 2 and 5
```

> [!WARNING]
> `.index()` raises a `ValueError` if the item is not found. Always wrap in `try/except` or check with `in` first.

```python
fruits = ("apple", "banana", "mango")

# Safe index lookup
target = "grape"
if target in fruits:
    print(fruits.index(target))
else:
    print(f"{target} not found")
```

### Built-in Functions That Work on Tuples

```python
nums = (3, 1, 4, 1, 5, 9, 2, 6)

print(len(nums))      # 8
print(min(nums))      # 1
print(max(nums))      # 9
print(sum(nums))      # 31
print(sorted(nums))   # [1, 1, 2, 3, 4, 5, 6, 9]  — returns a list
print(reversed(nums)) # iterator — use list() or loop to see values
print(3 in nums)      # True
print(7 in nums)      # False
```

### All Tuple Operations at a Glance

| Operation | Syntax | Returns |
|-----------|--------|---------|
| Length | `len(t)` | `int` |
| Minimum | `min(t)` | item |
| Maximum | `max(t)` | item |
| Sum | `sum(t)` | number |
| Sorted | `sorted(t)` | `list` |
| Count | `t.count(x)` | `int` |
| Index | `t.index(x)` | `int` |
| Membership | `x in t` | `bool` |
| Concatenate | `t1 + t2` | `tuple` |
| Repeat | `t * n` | `tuple` |
| Slice | `t[a:b]` | `tuple` |

---

## 7. Tuple Packing & Unpacking

Packing and unpacking are among the most useful and elegant features of Python tuples.

### Packing

Collecting multiple values into a single tuple.

```python
# Explicit parentheses
point = (10, 20, 30)

# Implicit — no parentheses needed
coords = 10, 20, 30
print(type(coords))   # <class 'tuple'>
```

### Basic Unpacking

Destructuring a tuple into individual variables. The number of variables must match the number of items.

```python
point = (10, 20, 30)
x, y, z = point
print(x, y, z)   # 10 20 30

# Swap two variables — classic Pythonic trick
a, b = 5, 10
a, b = b, a
print(a, b)      # 10 5

# Unpack a function's return value
def get_dimensions():
    return 1920, 1080

width, height = get_dimensions()
print(f"{width}x{height}")   # 1920x1080
```

### Extended Unpacking with `*`

Use `*` to collect multiple items into a list when you do not know how many there are.

```python
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*beginning, last = (1, 2, 3, 4, 5)
print(beginning)  # [1, 2, 3, 4]
print(last)       # 5

first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5
```

### Ignoring Values with `_`

Use `_` by convention to discard values you do not need.

```python
name, _, city = ("Haseeb", 25, "Karachi")   # ignore age
print(name, city)   # Haseeb Karachi

# Discard multiple values
first, *_, last = (1, 2, 3, 4, 5, 6, 7)
print(first, last)   # 1 7
```

### Unpacking in Loops

```python
students = [
    ("Alice", 88),
    ("Bob",   95),
    ("Carol", 72),
]

for name, score in students:
    print(f"{name}: {score}")

# Nested tuple unpacking in a loop
records = [("Alice", (25, "NYC")), ("Bob", (30, "LA"))]
for name, (age, city) in records:
    print(f"{name} is {age} from {city}")
```

### Unpacking Function Arguments with `*`

```python
def add(a, b, c):
    return a + b + c

nums = (10, 20, 30)
result = add(*nums)   # unpacks tuple as positional arguments
print(result)         # 60
```

---

## 8. Iterating Over Tuples

Tuples support all the same iteration patterns as lists.

### Basic `for` Loop

```python
colors = ("red", "green", "blue", "yellow")

for color in colors:
    print(color)
```

### With Index using `enumerate()`

```python
fruits = ("apple", "banana", "mango")

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start index from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

### Iterating Two Tuples in Parallel with `zip()`

```python
names  = ("Alice", "Bob", "Charlie")
scores = (88, 95, 72)

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

### Iterating in Reverse

```python
items = (1, 2, 3, 4, 5)

for item in reversed(items):
    print(item)   # 5 4 3 2 1
```

### `while` Loop with Index

```python
data = (10, 20, 30, 40, 50)
i = 0
while i < len(data):
    print(data[i])
    i += 1
```

### Iterating Nested Tuples

```python
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

---

## 9. Tuples as Dictionary Keys

One of the most powerful and unique advantages of tuples over lists — because tuples are **hashable** (when all their elements are hashable), they can be used as dictionary keys or stored in sets. Lists cannot.

```python
# Using tuples as dictionary keys
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278):  "London",
    (35.6762, 139.6503): "Tokyo",
}

print(locations[(40.7128, -74.0060)])   # New York

# Grid coordinates
grid = {}
grid[(0, 0)] = "start"
grid[(3, 4)] = "end"
grid[(1, 2)] = "checkpoint"

print(grid[(1, 2)])   # checkpoint
```

### Using Tuples in Sets

```python
# Set of coordinate pairs
visited = {(0, 0), (1, 2), (3, 4)}

if (1, 2) in visited:
    print("Already visited this cell")

visited.add((5, 6))
```

### Counting with Tuple Keys

```python
# Count word-position pairs
text = "the cat sat on the mat"
words = text.split()

position_map = {}
for i, word in enumerate(words):
    key = (word, i)
    position_map[key] = True

# Multi-dimensional key grouping
sales = {}
sales[("Q1", "North")] = 15000
sales[("Q1", "South")] = 12000
sales[("Q2", "North")] = 18000

for (quarter, region), amount in sales.items():
    print(f"{quarter} {region}: ${amount:,}")
```

> [!TIP]
> Using tuples as dict keys is the idiomatic Python way to build a multi-key lookup table. It is far cleaner than nested dicts for many use cases.

---

## 10. Named Tuples

A named tuple lets you access items by **name** instead of index, making your code far more readable while keeping all the performance benefits of a regular tuple.

### Using `collections.namedtuple`

```python
from collections import namedtuple

# Define a named tuple type
Point = namedtuple("Point", ["x", "y"])
Person = namedtuple("Person", ["name", "age", "city"])

# Create instances
p = Point(10, 20)
dev = Person("Haseeb", 25, "Karachi")

# Access by name — readable
print(p.x)         # 10
print(p.y)         # 20
print(dev.name)    # Haseeb
print(dev.city)    # Karachi

# Also works by index — backward compatible
print(p[0])        # 10
print(dev[1])      # 25

# Unpacking works too
name, age, city = dev
```

### Named Tuple Features

```python
Person = namedtuple("Person", ["name", "age", "city"])
dev = Person("Haseeb", 25, "Karachi")

# _asdict() — convert to dict
print(dev._asdict())
# {'name': 'Haseeb', 'age': 25, 'city': 'Karachi'}

# _replace() — create a modified copy (original unchanged)
updated = dev._replace(age=26, city="Lahore")
print(dev)      # Person(name='Haseeb', age=25, city='Karachi')
print(updated)  # Person(name='Haseeb', age=26, city='Lahore')

# _fields — inspect field names
print(Person._fields)   # ('name', 'age', 'city')

# _make() — create from an iterable
data = ["Alice", 30, "NYC"]
alice = Person._make(data)
print(alice)    # Person(name='Alice', age=30, city='NYC')
```

### Using `typing.NamedTuple` — Modern Style

```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
    z: float = 0.0   # default value

class Employee(NamedTuple):
    name: str
    department: str
    salary: float
    active: bool = True

p = Point(1.5, 2.5)
emp = Employee("Haseeb", "Engineering", 85000.0)

print(p)        # Point(x=1.5, y=2.5, z=0.0)
print(emp)      # Employee(name='Haseeb', department='Engineering', salary=85000.0, active=True)
print(emp.salary)   # 85000.0
```

> [!TIP]
> Prefer `typing.NamedTuple` over `collections.namedtuple` in modern Python. It supports type hints, default values, and reads like a normal class definition. It is essentially a lightweight, immutable data class.

### Named Tuple vs Dict vs Dataclass

| Feature | Named Tuple | Dict | Dataclass |
|---------|-------------|------|-----------|
| Access by name | ✅ Yes | ✅ Yes | ✅ Yes |
| Immutable | ✅ Yes | ❌ No | ❌ No (by default) |
| Unpackable | ✅ Yes | ❌ No | ❌ No |
| Memory efficient | ✅ Yes | ❌ No | Moderate |
| Type hints | ✅ Yes | ❌ No | ✅ Yes |
| Default values | ✅ Yes (NamedTuple) | ✅ Yes | ✅ Yes |
| Methods | ❌ No | ❌ No | ✅ Yes |

---

## 11. Tuples vs Lists

Knowing when to use a tuple and when to use a list is a mark of a mature Python developer.

### Side-by-Side Comparison

| Feature | Tuple | List |
|---------|-------|------|
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Mutable | ❌ No | ✅ Yes |
| Ordered | ✅ Yes | ✅ Yes |
| Indexed | ✅ Yes | ✅ Yes |
| Allows duplicates | ✅ Yes | ✅ Yes |
| Hashable | ✅ Yes (if elements are) | ❌ No |
| Dict key | ✅ Yes | ❌ No |
| Set member | ✅ Yes | ❌ No |
| Methods | 2 (`.count`, `.index`) | 11 |
| Memory | Less | More |
| Speed | Faster | Slightly slower |
| Use for | Fixed data, records | Dynamic sequences |

### When to Use a Tuple

```python
# Fixed collections that should never change
DAYS_OF_WEEK  = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
HTTP_METHODS  = ("GET", "POST", "PUT", "PATCH", "DELETE")
PRIMARY_COLORS = ("red", "yellow", "blue")

# Coordinates and geometric data
point_2d = (10.5, 20.3)
point_3d = (10.5, 20.3, 5.0)
bounding_box = (0, 0, 1920, 1080)   # x, y, width, height

# Database records / rows
user_record = (1, "Haseeb", "haseeb@email.com", "2024-01-15")

# Function returning multiple values
def get_stats(data):
    return min(data), max(data), sum(data) / len(data)

low, high, avg = get_stats([4, 8, 2, 9, 1])

# Dictionary keys
location_names = {(40.7128, -74.0060): "New York"}
```

### When to Use a List

```python
# Collections that grow or shrink
cart = []
cart.append("apple")
cart.remove("apple")

# Data that changes over time
active_users = ["Alice", "Bob"]
active_users.append("Charlie")

# When you need sorting in place
scores = [88, 72, 95, 61]
scores.sort()

# When you need list-specific methods
tasks = ["design", "develop", "test", "deploy"]
tasks.insert(1, "plan")
```

---

## 12. Performance & Memory

Tuples are measurably faster and lighter than lists. Understanding why helps you make better decisions.

### Memory Usage

```python
import sys

lst   = [1, 2, 3, 4, 5]
tup   = (1, 2, 3, 4, 5)

print(sys.getsizeof(lst))   # 104 bytes
print(sys.getsizeof(tup))   #  80 bytes  — ~23% less memory
```

### Creation Speed

```python
import timeit

list_time  = timeit.timeit("[1, 2, 3, 4, 5]", number=10_000_000)
tuple_time = timeit.timeit("(1, 2, 3, 4, 5)", number=10_000_000)

print(f"List:  {list_time:.3f}s")
print(f"Tuple: {tuple_time:.3f}s")
# Tuple is typically 2-5x faster to create
```

### Why Tuples are Faster

Python can **constant-fold** tuples of literals at compile time. A tuple of constants is stored as a single bytecode constant, while a list literal is rebuilt every time the code runs.

```python
import dis

# Tuple of constants — compiled to a single LOAD_CONST
dis.dis("(1, 2, 3)")
# LOAD_CONST  (1, 2, 3)   ← single operation

# List of constants — BUILD_LIST at runtime each time
dis.dis("[1, 2, 3]")
# LOAD_CONST  1
# LOAD_CONST  2
# LOAD_CONST  3
# BUILD_LIST  ← multiple operations
```

### Iteration Speed

```python
import timeit

lst = list(range(1000))
tup = tuple(range(1000))

list_iter  = timeit.timeit("for x in lst: pass", globals={"lst": lst}, number=100_000)
tuple_iter = timeit.timeit("for x in tup: pass", globals={"tup": tup}, number=100_000)

print(f"List iteration:  {list_iter:.3f}s")
print(f"Tuple iteration: {tuple_iter:.3f}s")
# Tuple iteration is consistently faster
```

### Performance Summary

| Operation | Tuple | List | Winner |
|-----------|-------|------|--------|
| Creation | Faster | Slower | Tuple |
| Memory usage | Less | More | Tuple |
| Iteration | Faster | Slightly slower | Tuple |
| Index access | Equal | Equal | Tie |
| Append / extend | N/A | O(1) amortized | List |
| Insert at index | N/A | O(n) | List |
| Hashing (dict key) | O(n) | Not supported | Tuple |

> [!TIP]
> In hot code paths — tight loops, large data processing, frequently called functions — prefer tuples over lists when the data is fixed. The speed and memory gains add up at scale.

---

## 13. Best Practices & Real-World Patterns

### Use Tuples for Function Return Values

```python
# Returning multiple values — Python packs them as a tuple
def divide(a, b):
    if b == 0:
        return None, "Division by zero"
    return a / b, None

result, error = divide(10, 2)
if error:
    print(f"Error: {error}")
else:
    print(f"Result: {result}")
```

### Use Tuples as Constants

```python
# Module-level constants — communicates intent that these never change
VALID_STATUSES  = ("pending", "active", "suspended", "closed")
ALLOWED_FORMATS = ("jpg", "png", "webp", "svg")
API_VERSIONS    = ("v1", "v2", "v3")

def validate_status(status: str) -> bool:
    return status in VALID_STATUSES
```

### Destructuring for Readability

```python
# Instead of magic indexes
raw = (1920, 1080, 60, "sRGB")
width, height, fps, color_space = raw

# Much clearer than raw[0], raw[1], raw[2]...
aspect = width / height
```

### Named Tuples for Structured Records

```python
from typing import NamedTuple

class GitCommit(NamedTuple):
    sha: str
    author: str
    message: str
    timestamp: str

commits = [
    GitCommit("a1b2c3", "Haseeb", "feat: add dark mode", "2024-01-15"),
    GitCommit("d4e5f6", "Alice",  "fix: nav overflow",   "2024-01-16"),
]

for commit in commits:
    print(f"[{commit.sha[:6]}] {commit.author}: {commit.message}")
```

### Tuple as a Composite Dict Key

```python
# Cache with (function_name, args) as key
cache = {}

def expensive_call(x, y):
    key = ("expensive_call", x, y)
    if key not in cache:
        cache[key] = x ** y + y ** x   # simulate expensive work
    return cache[key]
```

### Common Pitfalls to Avoid

```python
# 1. Forgetting the trailing comma on single-item tuples
x = (5)    # int, NOT a tuple
x = (5,)   # tuple — correct

# 2. Trying to mutate a tuple
t = (1, 2, 3)
t[0] = 99   # TypeError — convert to list first if you need to modify

# 3. Assuming tuples with mutable elements are fully immutable
t = ([1, 2], [3, 4])
t[0].append(99)
print(t)   # ([1, 2, 99], [3, 4])  — inner list mutated!

# 4. Using a list when data is fixed — missed performance opportunity
# Bad
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Good
DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
```

---

## Quick Reference Cheat Sheet

```python
# ── CREATING ──────────────────────────────────────────
t = ()                          # empty tuple
t = (42,)                       # single item — trailing comma required!
t = (1, 2, 3)                   # literal
t = 1, 2, 3                     # packing — no parentheses needed
t = tuple([1, 2, 3])            # from list
t = tuple(range(5))             # from range
t = tuple("abc")                # from string → ('a', 'b', 'c')

# ── ACCESSING ─────────────────────────────────────────
t[0]           # first item
t[-1]          # last item
t[i]           # item at index i

# ── SLICING ───────────────────────────────────────────
t[a:b]         # items a to b (exclusive)
t[a:b:step]    # with step
t[::-1]        # reversed
t[:]           # full copy

# ── METHODS ───────────────────────────────────────────
t.count(x)     # count occurrences of x
t.index(x)     # index of first x

# ── BUILT-INS ─────────────────────────────────────────
len(t)         # number of items
min(t)         # smallest item
max(t)         # largest item
sum(t)         # total
sorted(t)      # new sorted list
x in t         # membership test

# ── UNPACKING ─────────────────────────────────────────
a, b, c = t                    # basic unpacking
a, *rest = t                   # extended — rest is a list
*start, z = t                  # collect beginning
a, *mid, z = t                 # collect middle
a, _, c = t                    # ignore with _
func(*t)                       # unpack as function args

# ── OPERATIONS ────────────────────────────────────────
t1 + t2        # concatenate — new tuple
t * n          # repeat — new tuple

# ── NAMED TUPLES ──────────────────────────────────────
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p = Point(1.0, 2.0)
p.x              # access by name
p[0]             # access by index
x, y = p         # unpack
p._replace(x=5)  # modified copy
p._asdict()      # convert to dict
```

---

<div align="center">

**Python Tuples Reference** — Made with 💚 by Haseeb

*Python 3.10+ · Feel free to fork and star ⭐*

</div>
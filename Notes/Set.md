# 🐍 Python Sets — The Complete Guide

> Everything you need to know about one of Python's most underrated built-in data structures.

---

## Table of Contents

1. [What is a Set?](#what-is-a-set)
2. [Creating Sets](#creating-sets)
3. [Set Characteristics](#set-characteristics)
4. [Adding and Removing Elements](#adding-and-removing-elements)
5. [Set Operations](#set-operations)
6. [Set Methods — Full Reference](#set-methods--full-reference)
7. [Frozen Sets](#frozen-sets)
8. [Set Comprehensions](#set-comprehensions)
9. [Iterating Over Sets](#iterating-over-sets)
10. [Sets vs Other Data Structures](#sets-vs-other-data-structures)
11. [Performance and Time Complexity](#performance-and-time-complexity)
12. [Real-World Use Cases](#real-world-use-cases)
13. [Common Mistakes](#common-mistakes)
14. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## What is a Set?

A **set** in Python is an unordered collection of **unique**, **hashable** elements. Think of it like a mathematical set — no duplicates allowed, and the order doesn't matter.

```python
fruits = {"apple", "banana", "cherry"}
print(fruits)  # {'banana', 'cherry', 'apple'} — order may vary
```

Sets are defined using curly braces `{}` or the built-in `set()` constructor. Under the hood, Python implements sets using a **hash table**, which is why lookups are blazing fast.

---

## Creating Sets

### Using curly braces

```python
colors = {"red", "green", "blue"}
```

### Using the `set()` constructor

```python
numbers = set([1, 2, 3, 4, 5])
chars = set("hello")  # {'h', 'e', 'l', 'o'} — duplicates removed
empty_set = set()     # NOT {} — that creates an empty dict!
```

> **Important:** To create an empty set, you MUST use `set()`. Using `{}` gives you an empty dictionary.

```python
empty_dict = {}       # <class 'dict'>
empty_set  = set()    # <class 'set'>
```

### From other iterables

```python
from_tuple  = set((1, 2, 3))
from_range  = set(range(10))
from_string = set("Python")  # {'P', 'y', 't', 'h', 'o', 'n'}
```

---

## Set Characteristics

| Property | Description |
|---|---|
| **Unordered** | Elements have no index or guaranteed order |
| **Unique** | Duplicate values are automatically discarded |
| **Mutable** | You can add/remove elements after creation |
| **Hashable elements** | Elements must be immutable (strings, numbers, tuples) |

```python
# Duplicates are automatically removed
data = {1, 2, 2, 3, 3, 3}
print(data)  # {1, 2, 3}

# You cannot index a set
s = {10, 20, 30}
# s[0]  <-- TypeError: 'set' object is not subscriptable

# Unhashable types (like lists) cannot be set elements
# bad = {[1, 2], [3, 4]}  <-- TypeError
good = {(1, 2), (3, 4)}   # tuples are fine
```

---

## Adding and Removing Elements

### Adding elements

```python
s = {1, 2, 3}

s.add(4)           # adds a single element
print(s)           # {1, 2, 3, 4}

s.add(2)           # adding a duplicate — nothing happens
print(s)           # {1, 2, 3, 4}

s.update([5, 6, 7])         # add multiple elements from an iterable
s.update({8}, (9,), [10])   # works with any iterable type
```

### Removing elements

```python
s = {1, 2, 3, 4, 5}

s.remove(3)     # removes element — raises KeyError if not found
s.discard(10)   # removes element — does NOT raise error if missing (safer)
popped = s.pop()  # removes and returns an arbitrary element
s.clear()         # removes all elements, set becomes empty: set()
```

> **Tip:** Prefer `discard()` over `remove()` when you are not sure if the element exists. It is cleaner and avoids try/except boilerplate.

---

## Set Operations

This is where sets really shine. Python supports all the classic mathematical set operations, both as methods and as operators.

### Union — all elements from both sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)          # {1, 2, 3, 4, 5}
print(a.union(b))     # {1, 2, 3, 4, 5}
```

### Intersection — elements common to both sets

```python
print(a & b)               # {3}
print(a.intersection(b))   # {3}
```

### Difference — elements in `a` but not in `b`

```python
print(a - b)             # {1, 2}
print(a.difference(b))   # {1, 2}
```

### Symmetric Difference — elements in either set, but not both

```python
print(a ^ b)                        # {1, 2, 4, 5}
print(a.symmetric_difference(b))    # {1, 2, 4, 5}
```

### Subset and Superset

```python
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))    # True  — all of x is in y
print(x <= y)           # True  — same thing
print(x < y)            # True  — proper subset (x != y)

print(y.issuperset(x))  # True  — y contains all of x
print(y >= x)           # True  — same thing
```

### Disjoint — do the sets share any elements?

```python
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))  # True — no common elements
```

### In-place operations

These modify the original set instead of returning a new one:

```python
a = {1, 2, 3}
b = {3, 4, 5}

a |= b   # a.update(b) — union in-place
a &= b   # a.intersection_update(b)
a -= b   # a.difference_update(b)
a ^= b   # a.symmetric_difference_update(b)
```

---

## Set Methods — Full Reference

| Method | Description |
|---|---|
| `add(elem)` | Adds a single element |
| `update(*iterables)` | Adds elements from one or more iterables |
| `remove(elem)` | Removes element, raises `KeyError` if not found |
| `discard(elem)` | Removes element, no error if not found |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |
| `copy()` | Returns a shallow copy of the set |
| `union(*others)` | Returns a new set with all elements |
| `intersection(*others)` | Returns a new set with common elements |
| `difference(*others)` | Returns elements not in others |
| `symmetric_difference(other)` | Returns elements in either but not both |
| `issubset(other)` | Returns `True` if all elements are in `other` |
| `issuperset(other)` | Returns `True` if set contains all of `other` |
| `isdisjoint(other)` | Returns `True` if no elements are shared |
| `intersection_update(*others)` | Keeps only common elements in-place |
| `difference_update(*others)` | Removes elements found in others in-place |
| `symmetric_difference_update(other)` | Keeps non-shared elements in-place |

---

## Frozen Sets

A `frozenset` is an **immutable** version of a set. Once created, you cannot add or remove elements. This makes it hashable, so you can use it as a dictionary key or as an element inside another set.

```python
fs = frozenset([1, 2, 3, 4])
print(fs)         # frozenset({1, 2, 3, 4})

# You can still do all the read-only operations
print(2 in fs)    # True
print(fs | {5})   # frozenset({1, 2, 3, 4, 5}) — returns a new frozenset

# But mutations are blocked
# fs.add(5)   <-- AttributeError

# Use as a dictionary key
lookup = {frozenset({1, 2}): "pair", frozenset({3, 4, 5}): "trio"}
```

> **When to use frozenset:** Use it when you want a set that should not be modified, or when you need to store a set as a dict key or inside another set.

---

## Set Comprehensions

Just like list and dict comprehensions, Python supports set comprehensions with a clean, expressive syntax.

```python
# Basic set comprehension
squares = {x**2 for x in range(10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With a condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
# {0, 4, 16, 36, 64}

# From a string — unique characters, uppercased
unique_chars = {c.upper() for c in "hello world" if c != " "}
# {'H', 'E', 'L', 'O', 'W', 'R', 'D'}
```

Set comprehensions are a great way to build unique collections from existing data without any manual duplicate filtering.

---

## Iterating Over Sets

You can loop over a set like any other iterable, but remember there is no guaranteed order.

```python
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)

# Check membership (this is O(1) — very fast)
if "apple" in fruits:
    print("Found it!")

# Get the length
print(len(fruits))  # 3
```

If you need sorted output, use the `sorted()` function:

```python
for fruit in sorted(fruits):
    print(fruit)  # alphabetical order: apple, banana, cherry
```

---

## Sets vs Other Data Structures

| Feature | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Ordered | Yes | Yes | No | Yes (Python 3.7+) |
| Indexed | Yes | Yes | No | By key |
| Duplicates allowed | Yes | Yes | No | Keys: No, Values: Yes |
| Mutable | Yes | No | Yes | Yes |
| Hashable | No | Yes | No | No |
| Lookup speed | O(n) | O(n) | O(1) | O(1) |

**Use a set when:**
- You need fast membership testing (`in` operator)
- You want to automatically eliminate duplicates
- You need to perform set math (union, intersection, difference)
- Order does not matter

---

## Performance and Time Complexity

One of the biggest reasons to reach for sets is their O(1) average time complexity for the most common operations.

| Operation | Average Case | Worst Case |
|---|---|---|
| `x in s` | O(1) | O(n) |
| `s.add(x)` | O(1) | O(n) |
| `s.remove(x)` | O(1) | O(n) |
| `s.union(t)` | O(len(s) + len(t)) | |
| `s.intersection(t)` | O(min(len(s), len(t))) | |
| `s.difference(t)` | O(len(s)) | |
| `len(s)` | O(1) | |

```python
import time

big_list = list(range(1_000_000))
big_set  = set(range(1_000_000))

# List membership — O(n), slow
start = time.time()
999_999 in big_list
print(f"List: {time.time() - start:.6f}s")

# Set membership — O(1), near instant
start = time.time()
999_999 in big_set
print(f"Set:  {time.time() - start:.6f}s")
```

---

## Real-World Use Cases

### 1. Removing duplicates from a list

```python
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
# Note: this does NOT preserve order

# Preserve insertion order (Python 3.7+)
seen = set()
unique_ordered = [x for x in names if not (x in seen or seen.add(x))]
```

### 2. Fast membership testing

```python
BANNED_WORDS = {"spam", "scam", "fake"}

def is_safe(text):
    words = set(text.lower().split())
    return words.isdisjoint(BANNED_WORDS)

print(is_safe("buy this scam product"))  # False
print(is_safe("hello world"))            # True
```

### 3. Finding common elements between two datasets

```python
team_a = {"Alice", "Bob", "Carol", "Dave"}
team_b = {"Dave", "Eve", "Frank", "Alice"}

both_teams  = team_a & team_b   # {'Alice', 'Dave'}
only_team_a = team_a - team_b   # {'Bob', 'Carol'}
all_members = team_a | team_b   # everyone
```

### 4. Tagging and categorization systems

```python
user_permissions = {"read", "write"}
required_perms   = {"read", "write", "delete"}

if not required_perms.issubset(user_permissions):
    missing = required_perms - user_permissions
    print(f"Access denied. Missing permissions: {missing}")
    # Access denied. Missing permissions: {'delete'}
```

### 5. Graph algorithms — visited node tracking

```python
def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph.get(node, []))

    return visited
```

---

## Common Mistakes

### Mistake 1: Using `{}` for an empty set

```python
# Wrong
empty = {}
print(type(empty))  # <class 'dict'>

# Right
empty = set()
print(type(empty))  # <class 'set'>
```

### Mistake 2: Assuming order is preserved

```python
s = {3, 1, 4, 1, 5, 9}
print(list(s))  # could be [1, 3, 4, 5, 9] or any order — do not rely on it
```

### Mistake 3: Trying to add mutable types

```python
# Wrong — lists are not hashable
s = set()
s.add([1, 2, 3])   # TypeError: unhashable type: 'list'

# Right — use tuples instead
s.add((1, 2, 3))   # works fine
```

### Mistake 4: Modifying a set while iterating over it

```python
# Wrong — RuntimeError: Set changed size during iteration
s = {1, 2, 3, 4, 5}
for x in s:
    if x % 2 == 0:
        s.remove(x)

# Right — iterate over a copy
for x in s.copy():
    if x % 2 == 0:
        s.remove(x)
```

### Mistake 5: Confusing `difference` direction

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)  # {1}   — in a, not in b
print(b - a)  # {4}   — in b, not in a
```

---

## Quick Cheat Sheet

```python
# Create
s = {1, 2, 3}
s = set([1, 2, 3])
s = set()              # empty set

# Add / Remove
s.add(4)
s.update([5, 6])
s.remove(4)            # KeyError if missing
s.discard(4)           # safe, no error
s.pop()                # removes arbitrary element
s.clear()

# Membership
3 in s                 # True
3 not in s             # False

# Set Math
a | b                  # union
a & b                  # intersection
a - b                  # difference
a ^ b                  # symmetric difference

# Comparisons
a == b                 # equal sets?
a <= b                 # a is subset of b?
a >= b                 # a is superset of b?
a.isdisjoint(b)        # no common elements?

# Copy
s2 = s.copy()

# Frozenset
fs = frozenset([1, 2, 3])

# Comprehension
s = {x**2 for x in range(10)}
```

---

## Further Reading

- [Python Docs — Built-in Types: set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Python Docs — Data Structures](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Time Complexity — Python Wiki](https://wiki.python.org/moin/TimeComplexity)

---

*Written for Python 3.7+. All examples tested and working.*
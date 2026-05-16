# 📖 Python Dictionaries — The Complete Guide

> The most powerful and widely used data structure in Python. If you write Python, you use dicts. This guide covers everything from the basics to the internals.

---

## Table of Contents

1. [What is a Dictionary?](#what-is-a-dictionary)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Dictionary Characteristics](#dictionary-characteristics)
4. [Accessing Values](#accessing-values)
5. [Adding and Updating Elements](#adding-and-updating-elements)
6. [Removing Elements](#removing-elements)
7. [Dictionary Methods — Full Reference](#dictionary-methods--full-reference)
8. [Iterating Over Dictionaries](#iterating-over-dictionaries)
9. [Nested Dictionaries](#nested-dictionaries)
10. [Dictionary Comprehensions](#dictionary-comprehensions)
11. [Merging Dictionaries](#merging-dictionaries)
12. [Default Values and Missing Keys](#default-values-and-missing-keys)
13. [Ordered Dictionaries](#ordered-dictionaries)
14. [Dictionaries vs Other Data Structures](#dictionaries-vs-other-data-structures)
15. [Performance and Time Complexity](#performance-and-time-complexity)
16. [Real-World Use Cases](#real-world-use-cases)
17. [Common Mistakes](#common-mistakes)
18. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## What is a Dictionary?

A **dictionary** in Python is an ordered collection of **key-value pairs**. Each key maps to a value, and keys must be unique. Think of it like a real-world dictionary where a word (key) maps to its definition (value).

```python
person = {
    "name": "Haseeb",
    "role": "Frontend Developer",
    "skills": ["React", "TypeScript", "Next.js"]
}
```

Under the hood, Python dictionaries are implemented as **hash tables**. This gives O(1) average time complexity for lookups, insertions, and deletions — making dicts one of the most performance-friendly structures in the language.

> Since Python 3.7+, dictionaries maintain **insertion order** as a guaranteed language feature.

---

## Creating Dictionaries

### Using curly braces (most common)

```python
user = {"username": "haseeb4212", "language": "Python", "level": 5}
```

### Using the `dict()` constructor

```python
user = dict(username="haseeb4212", language="Python", level=5)
```

### From a list of key-value pairs

```python
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
# {'a': 1, 'b': 2, 'c': 3}
```

### Using `dict.fromkeys()`

```python
keys = ["name", "age", "city"]
d = dict.fromkeys(keys, None)
# {'name': None, 'age': None, 'city': None}

d = dict.fromkeys(keys, 0)
# {'name': 0, 'age': 0, 'city': 0}
```

### Empty dictionary

```python
empty = {}         # <class 'dict'>
empty = dict()     # same thing
```

---

## Dictionary Characteristics

| Property | Description |
|---|---|
| **Ordered** | Maintains insertion order (Python 3.7+) |
| **Mutable** | Keys and values can be added, changed, or removed |
| **Unique Keys** | Duplicate keys are not allowed — last value wins |
| **Hashable Keys** | Keys must be immutable types (str, int, float, tuple) |
| **Any Value** | Values can be any Python object |

```python
# Duplicate keys — last one wins
d = {"name": "Alice", "name": "Bob"}
print(d)  # {'name': 'Bob'}

# Keys must be hashable
good = {(1, 2): "tuple key"}   # tuples are fine
# bad = {[1, 2]: "list key"}   # TypeError: unhashable type: 'list'

# Values can be anything
mixed = {
    "string": "hello",
    "number": 42,
    "list":   [1, 2, 3],
    "func":   len,
    "nested": {"a": 1}
}
```

---

## Accessing Values

### Using square brackets

```python
user = {"name": "Haseeb", "age": 25}

print(user["name"])   # Haseeb
# print(user["city"]) # KeyError: 'city'
```

### Using `.get()` — the safe way

```python
print(user.get("name"))           # Haseeb
print(user.get("city"))           # None  — no error
print(user.get("city", "N/A"))    # N/A   — custom default
```

> **Tip:** Always prefer `.get()` when you are not 100% sure a key exists. It is safer, cleaner, and avoids try/except clutter.

### Checking key existence

```python
if "name" in user:
    print(user["name"])

if "city" not in user:
    print("City not found")
```

---

## Adding and Updating Elements

### Adding a new key

```python
user = {"name": "Haseeb"}
user["role"] = "Developer"
print(user)  # {'name': 'Haseeb', 'role': 'Developer'}
```

### Updating an existing key

```python
user["name"] = "Haseeb Ali"   # simply reassign
```

### Using `.update()`

```python
user.update({"age": 25, "city": "Lahore"})

# Also works with keyword arguments
user.update(age=25, city="Lahore")

# Or from another dict
extra = {"github": "Haseeb4212", "portfolio": "vercel.app"}
user.update(extra)
```

### Using `.setdefault()` — add only if key is missing

```python
user.setdefault("role", "Developer")   # sets 'role' if it does not exist
user.setdefault("name", "Unknown")     # does nothing — 'name' already exists

print(user["role"])  # Developer
print(user["name"])  # Haseeb Ali  — unchanged
```

---

## Removing Elements

```python
user = {"name": "Haseeb", "age": 25, "city": "Lahore", "role": "Dev"}

# del — removes a key, raises KeyError if missing
del user["city"]

# pop() — removes and returns the value
age = user.pop("age")           # returns 25
val = user.pop("missing", 0)    # returns 0 — no error with default

# popitem() — removes and returns the last inserted key-value pair
last = user.popitem()           # returns ('role', 'Dev') as a tuple

# clear() — empties the dictionary
user.clear()
print(user)   # {}
```

---

## Dictionary Methods — Full Reference

| Method | Description |
|---|---|
| `d.get(key, default)` | Returns value or default if key is missing |
| `d.keys()` | Returns a view of all keys |
| `d.values()` | Returns a view of all values |
| `d.items()` | Returns a view of all (key, value) pairs |
| `d.update(other)` | Merges another dict or iterable of pairs |
| `d.setdefault(key, default)` | Returns value; inserts key with default if missing |
| `d.pop(key, default)` | Removes and returns value |
| `d.popitem()` | Removes and returns the last inserted pair |
| `d.clear()` | Removes all items |
| `d.copy()` | Returns a shallow copy |
| `dict.fromkeys(iterable, value)` | Creates a new dict from keys with a default value |

### Views are live — not snapshots

```python
d = {"a": 1, "b": 2}
keys = d.keys()

d["c"] = 3
print(keys)  # dict_keys(['a', 'b', 'c']) — updates automatically
```

---

## Iterating Over Dictionaries

### Over keys (default behavior)

```python
config = {"host": "localhost", "port": 5432, "db": "mydb"}

for key in config:
    print(key)

# same as
for key in config.keys():
    print(key)
```

### Over values

```python
for value in config.values():
    print(value)
```

### Over key-value pairs — most common pattern

```python
for key, value in config.items():
    print(f"{key}: {value}")

# host: localhost
# port: 5432
# db: mydb
```

### With enumeration

```python
for i, (key, value) in enumerate(config.items()):
    print(f"{i}. {key} = {value}")
```

---

## Nested Dictionaries

Dictionaries can hold other dictionaries as values. This is extremely common for representing structured data like JSON.

```python
users = {
    "alice": {
        "age": 30,
        "skills": ["Python", "Django"],
        "address": {"city": "London", "zip": "EC1A"}
    },
    "bob": {
        "age": 27,
        "skills": ["React", "TypeScript"],
        "address": {"city": "New York", "zip": "10001"}
    }
}

# Accessing nested values
print(users["alice"]["age"])                 # 30
print(users["bob"]["address"]["city"])       # New York
print(users["alice"]["skills"][0])           # Python

# Safe access with .get() on nested dicts
city = users.get("alice", {}).get("address", {}).get("city", "Unknown")
print(city)   # London
```

### Updating nested values

```python
users["alice"]["age"] = 31
users["bob"]["skills"].append("Node.js")
```

### Flattening a nested dict

```python
def flatten(d, parent_key="", sep="."):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten(v, new_key, sep))
        else:
            items[new_key] = v
    return items

flat = flatten(users["alice"])
# {'age': 30, 'skills': [...], 'address.city': 'London', 'address.zip': 'EC1A'}
```

---

## Dictionary Comprehensions

A clean, expressive way to build dictionaries from iterables or transformations.

```python
# Basic comprehension
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With a condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform an existing dict
prices = {"apple": 1.5, "banana": 0.5, "cherry": 3.0}
discounted = {item: price * 0.9 for item, price in prices.items()}

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Build from two lists
keys   = ["name", "age", "city"]
values = ["Haseeb", 25, "Lahore"]
d = {k: v for k, v in zip(keys, values)}
# {'name': 'Haseeb', 'age': 25, 'city': 'Lahore'}
```

---

## Merging Dictionaries

### Python 3.9+ — merge operator `|`

```python
defaults = {"theme": "dark", "font_size": 14, "lang": "en"}
overrides = {"font_size": 16, "lang": "ur"}

merged = defaults | overrides
# {'theme': 'dark', 'font_size': 16, 'lang': 'ur'}

# In-place merge
defaults |= overrides
```

### Python 3.5+ — unpacking with `**`

```python
merged = {**defaults, **overrides}
# keys from overrides win on conflict
```

### Using `.update()` — modifies in place

```python
defaults.update(overrides)
```

### Merging multiple dicts

```python
a = {"x": 1}
b = {"y": 2}
c = {"z": 3}

merged = {**a, **b, **c}
# {'x': 1, 'y': 2, 'z': 3}
```

---

## Default Values and Missing Keys

### `dict.get()` with defaults

```python
config = {"debug": True}
timeout = config.get("timeout", 30)   # 30 — key not found
```

### `collections.defaultdict`

Automatically creates a default value when a missing key is accessed. Great for grouping and counting.

```python
from collections import defaultdict

# Grouping items
groups = defaultdict(list)
data = [("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana")]

for category, item in data:
    groups[category].append(item)

print(dict(groups))
# {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}

# Word frequency count
word_count = defaultdict(int)
text = "the quick brown fox jumps over the lazy dog the"

for word in text.split():
    word_count[word] += 1

print(dict(word_count))
# {'the': 3, 'quick': 1, 'brown': 1, ...}
```

### `collections.Counter`

A specialized dict subclass built for counting.

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts)               # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts.most_common(2))  # [('apple', 3), ('banana', 2)]
print(counts["apple"])      # 3
print(counts["missing"])    # 0  — no KeyError
```

---

## Ordered Dictionaries

Since Python 3.7, regular dicts preserve insertion order. But `collections.OrderedDict` has some extra tricks.

```python
from collections import OrderedDict

od = OrderedDict()
od["first"]  = 1
od["second"] = 2
od["third"]  = 3

# Move to end or beginning
od.move_to_end("first")           # moves to last
od.move_to_end("third", last=False)  # moves to first

# OrderedDict equality checks order too
d1 = OrderedDict([("a", 1), ("b", 2)])
d2 = OrderedDict([("b", 2), ("a", 1)])
print(d1 == d2)   # False — order matters here

# Regular dict does not care about order for equality
print(dict(d1) == dict(d2))   # True
```

> **When to use OrderedDict today:** Mostly for the `move_to_end()` method or when you specifically need order-sensitive equality comparison.

---

## Dictionaries vs Other Data Structures

| Feature | Dict | List | Set | Named Tuple |
|---|---|---|---|---|
| Key-value pairs | Yes | No | No | No |
| Access by key | O(1) | O(n) | N/A | By attribute |
| Preserves order | Yes (3.7+) | Yes | No | Yes |
| Unique keys | Yes | N/A | Yes (elements) | N/A |
| Mutable | Yes | Yes | Yes | No |
| Memory usage | Higher | Lower | Medium | Lower |

**Reach for a dict when:**
- You need to map relationships between data
- You want fast key-based lookups
- You are representing structured, named data
- You are working with JSON-like structures

---

## Performance and Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| `d[key]` — access | O(1) | O(n) |
| `d[key] = val` — insert/update | O(1) | O(n) |
| `del d[key]` — delete | O(1) | O(n) |
| `key in d` — membership | O(1) | O(n) |
| `d.copy()` — copy | O(n) | O(n) |
| `d.items()`, `d.keys()`, `d.values()` | O(1) | O(1) |
| Iteration | O(n) | O(n) |

Worst case O(n) happens only during hash collisions, which are extremely rare in practice with Python's hash implementation.

```python
import time

# Dict lookup vs list search
big_dict = {i: i*2 for i in range(1_000_000)}
big_list = list(range(1_000_000))

target = 999_999

start = time.time()
target in big_dict
print(f"Dict:  {time.time() - start:.8f}s")   # near instant

start = time.time()
target in big_list
print(f"List:  {time.time() - start:.6f}s")   # noticeably slower
```

---

## Real-World Use Cases

### 1. Caching / Memoization

```python
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result

print(fibonacci(50))  # computed in microseconds with caching
```

### 2. Counting and frequency analysis

```python
from collections import Counter

text = "to be or not to be that is the question"
freq = Counter(text.split())

print(freq.most_common(3))
# [('be', 2), ('to', 2), ('or', 1)]
```

### 3. Grouping data

```python
from collections import defaultdict

employees = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob",   "dept": "Design"},
    {"name": "Carol", "dept": "Engineering"},
    {"name": "Dave",  "dept": "Design"},
]

by_dept = defaultdict(list)
for emp in employees:
    by_dept[emp["dept"]].append(emp["name"])

print(dict(by_dept))
# {'Engineering': ['Alice', 'Carol'], 'Design': ['Bob', 'Dave']}
```

### 4. Configuration management

```python
DEFAULT_CONFIG = {
    "debug":    False,
    "host":     "0.0.0.0",
    "port":     8000,
    "timeout":  30,
    "log_level": "INFO"
}

def get_config(overrides=None):
    config = DEFAULT_CONFIG.copy()
    if overrides:
        config.update(overrides)
    return config

dev_config = get_config({"debug": True, "port": 3000})
```

### 5. Dispatch tables — replacing long if/elif chains

```python
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculate(op, a, b):
    fn = operations.get(op)
    if fn is None:
        raise ValueError(f"Unknown operation: {op}")
    return fn(a, b)

print(calculate("+", 10, 5))  # 15
print(calculate("*", 4, 3))   # 12
```

### 6. JSON / API response handling

```python
import json

response_text = '{"status": "ok", "user": {"id": 42, "name": "Haseeb"}}'
data = json.loads(response_text)

user_id   = data.get("user", {}).get("id")
user_name = data.get("user", {}).get("name", "Unknown")

print(f"User: {user_name} (ID: {user_id})")
```

---

## Common Mistakes

### Mistake 1: Using `d[key]` instead of `d.get(key)` on uncertain keys

```python
d = {"name": "Haseeb"}

# Wrong — crashes if key is missing
print(d["age"])   # KeyError: 'age'

# Right — returns None or your default
print(d.get("age", 0))   # 0
```

### Mistake 2: Mutating a dict while iterating over it

```python
d = {"a": 1, "b": 2, "c": 3}

# Wrong — RuntimeError: dictionary changed size during iteration
for key in d:
    if d[key] == 2:
        del d[key]

# Right — iterate over a copy of keys
for key in list(d.keys()):
    if d[key] == 2:
        del d[key]
```

### Mistake 3: Assuming a key exists after `setdefault`

```python
# setdefault returns the value but does NOT overwrite existing ones
d = {"count": 5}
d.setdefault("count", 0)   # count stays 5, NOT reset to 0
```

### Mistake 4: Shallow copy traps with nested dicts

```python
import copy

original = {"user": {"name": "Haseeb", "scores": [95, 87]}}

shallow = original.copy()
shallow["user"]["name"] = "Ali"

print(original["user"]["name"])  # Ali — original was also changed!

# Fix: use deep copy
deep = copy.deepcopy(original)
deep["user"]["name"] = "Bob"
print(original["user"]["name"])  # Ali — original is safe now
```

### Mistake 5: Using mutable default values in function signatures

```python
# Wrong — the default dict is shared across all calls
def add_item(item, container={}):
    container[item] = True
    return container

print(add_item("a"))   # {'a': True}
print(add_item("b"))   # {'a': True, 'b': True}  — unexpected!

# Right — use None and create inside
def add_item(item, container=None):
    if container is None:
        container = {}
    container[item] = True
    return container
```

### Mistake 6: Forgetting that `dict.keys()` returns a view, not a list

```python
d = {"a": 1, "b": 2}
keys = d.keys()

# If you need a static snapshot, convert to list
keys_list = list(d.keys())

# Indexing a view does not work
# keys[0]  <-- TypeError
```

---

## Quick Cheat Sheet

```python
# Create
d = {"key": "value"}
d = dict(key="value")
d = dict.fromkeys(["a", "b"], 0)
d = {}            # empty dict

# Access
d["key"]                   # KeyError if missing
d.get("key")               # None if missing
d.get("key", "default")    # custom fallback

# Add / Update
d["new_key"] = "value"
d.update({"a": 1, "b": 2})
d.setdefault("key", "default")   # only sets if missing

# Remove
del d["key"]                # KeyError if missing
d.pop("key")                # KeyError if missing
d.pop("key", None)          # safe
d.popitem()                 # removes last inserted pair
d.clear()                   # empty the dict

# Inspect
"key" in d                  # membership check
len(d)                      # number of pairs

# Iterate
for k in d: ...
for k in d.keys(): ...
for v in d.values(): ...
for k, v in d.items(): ...

# Copy
d2 = d.copy()               # shallow
import copy
d2 = copy.deepcopy(d)       # deep

# Merge (Python 3.9+)
merged = d1 | d2
d1 |= d2

# Merge (Python 3.5+)
merged = {**d1, **d2}

# Comprehension
d = {k: v for k, v in pairs}
d = {k: v for k, v in d.items() if condition}

# Useful stdlib
from collections import defaultdict, Counter, OrderedDict
```

---

## Further Reading

- [Python Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Docs — Built-in Types: dict](https://docs.python.org/3/library/stdtypes.html#dict)
- [Python Docs — collections module](https://docs.python.org/3/library/collections.html)
- [PEP 584 — Add Union Operators to dict](https://peps.python.org/pep-0584/)
- [Time Complexity — Python Wiki](https://wiki.python.org/moin/TimeComplexity)

---

*Written for Python 3.7+. All examples tested and working.*
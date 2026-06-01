# 🐍 Python Cheat Sheet
> Quick reference for everything Python — bookmark this, you will need it

---

## 📌 Variables & Data Types

```python
# Numbers
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex

# String
name = "Haseeb"
multi = """line1
line2"""

# Boolean
is_dev = True
is_noob = False

# None
val = None

# Check type
type(x)         # <class 'int'>
isinstance(x, int)  # True
```

---

## 📌 String Operations

```python
s = "Hello, World!"

# Basic
len(s)              # 13
s.upper()           # HELLO, WORLD!
s.lower()           # hello, world!
s.strip()           # removes whitespace from both ends
s.lstrip()          # left strip
s.rstrip()          # right strip
s.replace("World", "Python")  # Hello, Python!
s.split(", ")       # ['Hello', 'World!']
", ".join(["a","b","c"])      # a, b, c
s.find("World")     # 7
s.count("l")        # 3
s.startswith("Hello")  # True
s.endswith("!")        # True
s.isdigit()         # False
s.isalpha()         # False
s.isupper()         # False
s.islower()         # False
s.title()           # Hello, World!
s.center(20, "-")   # ---Hello, World!---
s.zfill(5)          # pads with zeros

# Slicing
s[0]        # H
s[-1]       # !
s[0:5]      # Hello
s[::-1]     # !dlroW ,olleH  (reverse)
s[::2]      # Hlo ol  (every 2nd char)

# Formatting
f"My name is {name}"          # f-string (recommended)
"Hello {}".format("World")    # .format()
"Hello %s" % "World"          # % formatting (old style)

# Raw string (ignores escape chars)
path = r"C:\Users\haseeb"
```

---

## 📌 Numbers & Math

```python
# Arithmetic
10 + 3   # 13
10 - 3   # 7
10 * 3   # 30
10 / 3   # 3.3333 (float division)
10 // 3  # 3      (floor division)
10 % 3   # 1      (modulo)
2 ** 8   # 256    (power)

# Math module
import math
math.sqrt(16)     # 4.0
math.ceil(4.2)    # 5
math.floor(4.8)   # 4
math.pi           # 3.14159...
math.e            # 2.71828...
math.abs(-5)      # use abs(-5) directly
math.log(100, 10) # 2.0
math.factorial(5) # 120

# Built-in
abs(-5)           # 5
round(3.14159, 2) # 3.14
pow(2, 10)        # 1024
divmod(10, 3)     # (3, 1)
max(1, 2, 3)      # 3
min(1, 2, 3)      # 1
sum([1,2,3,4])    # 10
```

---

## 📌 Type Conversion

```python
int("42")           # 42
int(3.9)            # 3  (truncates, no rounding)
float("3.14")       # 3.14
str(100)            # "100"
bool(0)             # False
bool("")            # False
bool([])            # False
bool(None)          # False
bool(1)             # True
bool("hello")       # True
list("abc")         # ['a', 'b', 'c']
tuple([1,2,3])      # (1, 2, 3)
set([1,1,2,3])      # {1, 2, 3}
dict([("a",1)])     # {'a': 1}
list(range(5))      # [0, 1, 2, 3, 4]
```

---

## 📌 Operators

```python
# Arithmetic:  +  -  *  /  //  %  **
# Comparison:  ==  !=  >  <  >=  <=
# Logical:     and  or  not
# Bitwise:     &  |  ^  ~  <<  >>
# Assignment:  =  +=  -=  *=  /=  //=  **=  %=
# Identity:    is  is not
# Membership:  in  not in

# Ternary
x = 10
label = "even" if x % 2 == 0 else "odd"

# Walrus operator (Python 3.8+)
if (n := len("hello")) > 3:
    print(n)   # 5
```

---

## 📌 List

```python
lst = [1, 2, 3, 4, 5]

# Access
lst[0]          # 1
lst[-1]         # 5
lst[1:3]        # [2, 3]
lst[::-1]       # [5, 4, 3, 2, 1]

# Modify
lst.append(6)           # add to end
lst.insert(0, 0)        # insert at index
lst.extend([7, 8])      # merge another list
lst.remove(3)           # remove first occurrence of value
lst.pop()               # remove and return last
lst.pop(0)              # remove and return at index
lst[0] = 99             # update value
del lst[0]              # delete at index

# Info
len(lst)                # length
lst.count(2)            # count occurrences
lst.index(4)            # index of first occurrence

# Sort
lst.sort()              # sort in-place (ascending)
lst.sort(reverse=True)  # sort in-place (descending)
sorted(lst)             # returns new sorted list
lst.reverse()           # reverse in-place

# Copy
lst.copy()              # shallow copy
lst[:]                  # shallow copy (slice)

# Check
3 in lst                # True
3 not in lst            # False

# Unpack
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2,3,4]
```

---

## 📌 Tuple

```python
t = (1, 2, 3)
t2 = 1, 2, 3         # parentheses optional
single = (1,)        # single item tuple needs trailing comma

t[0]                 # 1
t[-1]                # 3
t[1:3]               # (2, 3)
len(t)               # 3
t.count(2)           # 1
t.index(2)           # 1
t + (4, 5)           # (1, 2, 3, 4, 5)
t * 2                # (1, 2, 3, 1, 2, 3)

# Unpack
x, y, z = t
```

---

## 📌 Dictionary

```python
d = {"name": "Haseeb", "age": 22, "role": "Dev"}

# Access
d["name"]                  # Haseeb
d.get("name")              # Haseeb (safe, no KeyError)
d.get("salary", 0)         # 0 (default if missing)

# Modify
d["age"] = 23              # update
d["city"] = "Lahore"       # add new key
del d["role"]              # delete key
d.pop("age")               # remove and return value
d.popitem()                # remove last inserted item

# Info
len(d)                     # number of keys
d.keys()                   # dict_keys([...])
d.values()                 # dict_values([...])
d.items()                  # dict_items([...])

# Check
"name" in d                # True
"salary" in d              # False

# Merge
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}      # {'a': 1, 'b': 2}
d1.update(d2)              # updates d1 in-place

# Copy
d.copy()                   # shallow copy

# Loop
for key in d:
    print(key)
for key, val in d.items():
    print(key, val)
```

---

## 📌 Set

```python
s = {1, 2, 3, 4, 5}
empty = set()              # NOT {} (that is a dict)

# Modify
s.add(6)                   # add element
s.remove(3)                # remove (KeyError if missing)
s.discard(3)               # remove (no error if missing)
s.pop()                    # remove random element
s.clear()                  # empty the set

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
a | b                      # union        {1,2,3,4,5}
a & b                      # intersection {3}
a - b                      # difference   {1,2}
a ^ b                      # symmetric diff {1,2,4,5}

a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)

# Check
3 in s                     # True
a.issubset(b)              # False
a.issuperset(b)            # False
a.isdisjoint(b)            # False
```

---

## 📌 Control Flow

```python
# if / elif / else
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# for loop
for i in range(5):          # 0 1 2 3 4
    print(i)

for i in range(2, 10, 2):   # 2 4 6 8
    print(i)

for item in ["a", "b", "c"]:
    print(item)

for i, val in enumerate(["a","b","c"]):
    print(i, val)           # 0 a, 1 b, 2 c

for a, b in zip([1,2], [3,4]):
    print(a, b)             # 1 3, 2 4

# while loop
x = 0
while x < 5:
    x += 1

# Loop control
break       # exit loop
continue    # skip to next iteration
pass        # do nothing (placeholder)

# Loop with else (runs if no break)
for i in range(5):
    if i == 10:
        break
else:
    print("No break occurred")
```

---

## 📌 Functions

```python
# Basic
def greet(name):
    return f"Hello, {name}!"

# Default arguments
def greet(name, msg="Hi"):
    return f"{msg}, {name}"

# *args (variable positional)
def total(*args):
    return sum(args)
total(1, 2, 3, 4)   # 10

# **kwargs (variable keyword)
def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
show(name="Haseeb", role="Dev")

# Both
def func(*args, **kwargs):
    pass

# Return multiple values
def minmax(lst):
    return min(lst), max(lst)

lo, hi = minmax([3, 1, 4, 1, 5])

# Lambda
square = lambda x: x ** 2
add = lambda x, y: x + y

# Annotations (type hints)
def add(a: int, b: int) -> int:
    return a + b
```

---

## 📌 Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
flat = [n for row in [[1,2],[3,4]] for n in row]

# Dict comprehension
d = {x: x**2 for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Set comprehension
unique = {x % 3 for x in range(10)}

# Generator expression (lazy, memory efficient)
gen = (x**2 for x in range(1000))
total = sum(x**2 for x in range(1000))
```

---

## 📌 Lambda / Map / Filter / Reduce

```python
nums = [1, 2, 3, 4, 5]

# map — apply function to all
squares = list(map(lambda x: x**2, nums))
# [1, 4, 9, 16, 25]

# filter — keep matching elements
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4]

# reduce — collapse to single value
from functools import reduce
total = reduce(lambda x, y: x + y, nums)
# 15

# sorted with key
words = ["banana", "kiwi", "apple"]
sorted(words, key=len)           # by length
sorted(words, key=lambda w: w[-1])  # by last letter
```

---

## 📌 OOP

```python
class Animal:
    species = "Unknown"       # class variable

    def __init__(self, name, age):
        self.name = name      # instance variable
        self.__age = age      # private

    def speak(self):          # instance method
        return "..."

    @classmethod
    def info(cls):            # class method
        return cls.species

    @staticmethod
    def breathes():           # static method
        return True

    @property
    def age(self):            # getter
        return self.__age

    @age.setter
    def age(self, val):       # setter
        self.__age = val

    def __str__(self):        # print(obj)
        return f"{self.name}"

    def __repr__(self):       # repr(obj)
        return f"Animal({self.name})"

    def __len__(self):        return 1
    def __eq__(self, other):  return self.name == other.name
    def __add__(self, other): pass
    def __lt__(self, other):  pass


# Inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):          # override
        return "Woof!"


# Multiple Inheritance
class C(A, B):
    pass

C.__mro__   # Method Resolution Order


# Abstract class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2
```

---

## 📌 Decorators

```python
# Basic decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    return f"Hi {name}"

# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi(): print("Hi")

# functools.wraps (preserves metadata)
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Useful built-in decorators
@property       # getter
@staticmethod   # no self/cls
@classmethod    # cls instead of self
```

---

## 📌 Generators & Iterators

```python
# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
next(gen)   # 5
next(gen)   # 4

# Generator expression
squares = (x**2 for x in range(10))

# Custom iterator
class Counter:
    def __init__(self, start, end):
        self.cur = start
        self.end = end

    def __iter__(self): return self

    def __next__(self):
        if self.cur > self.end:
            raise StopIteration
        val = self.cur
        self.cur += 1
        return val

# itertools
import itertools

itertools.count(1)              # 1 2 3 4 ... (infinite)
itertools.cycle([1,2,3])        # 1 2 3 1 2 3 ... (infinite)
itertools.repeat(5, 3)          # 5 5 5
itertools.chain([1,2],[3,4])    # 1 2 3 4
itertools.islice(gen, 5)        # first 5 from generator
itertools.combinations("ABC",2) # AB AC BC
itertools.permutations("AB",2)  # AB BA
itertools.product([1,2],[3,4])  # cartesian product
```

---

## 📌 Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or Value error")
except Exception as e:
    print(f"Unknown: {e}")
else:
    print("No error")       # runs if no exception
finally:
    print("Always runs")    # cleanup

# Raise
raise ValueError("Bad input")

# Custom exception
class AppError(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code

# Common exceptions
# ValueError, TypeError, KeyError, IndexError
# AttributeError, FileNotFoundError
# ZeroDivisionError, ImportError
# StopIteration, RecursionError
# OverflowError, MemoryError, OSError
```

---

## 📌 File Handling

```python
# Read
with open("file.txt", "r") as f:
    content = f.read()          # entire file as string
    lines = f.readlines()       # list of lines
    line = f.readline()         # one line

# Write
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Append
with open("file.txt", "a") as f:
    f.write("More content\n")

# Binary
with open("image.png", "rb") as f:
    data = f.read()

# Modes
# r  → read (default)
# w  → write (overwrites)
# a  → append
# x  → create (fails if exists)
# b  → binary mode
# +  → read and write

# JSON
import json
with open("data.json", "w") as f:
    json.dump({"key": "val"}, f, indent=2)

with open("data.json", "r") as f:
    data = json.load(f)

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# OS operations
import os
os.getcwd()                   # current directory
os.listdir(".")               # list files
os.path.exists("file.txt")    # check existence
os.path.join("folder","file") # safe path join
os.makedirs("dir", exist_ok=True)
os.remove("file.txt")
os.rename("old.txt","new.txt")
```

---

## 📌 Modules & Packages

```python
import math
import os as operating_system
from datetime import datetime, timedelta
from collections import Counter, defaultdict, deque
from functools import wraps, reduce, lru_cache, partial
from itertools import chain, product, combinations
from typing import List, Dict, Optional, Union, Tuple, Any

# Useful standard library modules
import sys          # system operations
import re           # regex
import json         # JSON
import os           # OS operations
import time         # time
import datetime     # date and time
import random       # random numbers
import copy         # copy objects
import math         # math operations
import hashlib      # hashing
import uuid         # unique IDs
import pathlib      # path operations
import logging      # logging
import argparse     # CLI arguments
import subprocess   # run shell commands
import threading    # threads
import multiprocessing
import asyncio      # async
import socket       # networking
import http.client  # HTTP
import urllib       # URL tools
```

---

## 📌 Useful Built-ins

```python
# Type checking
type(x)
isinstance(x, int)
issubclass(Dog, Animal)

# Object info
dir(obj)            # list all attributes and methods
vars(obj)           # __dict__ of object
hasattr(obj, "name")
getattr(obj, "name", "default")
setattr(obj, "name", "value")
delattr(obj, "name")

# Iteration helpers
len([1,2,3])        # 3
range(5)            # 0-4
enumerate(lst)      # (index, value) pairs
zip(a, b)           # pairs from two iterables
map(fn, lst)        # apply fn to each
filter(fn, lst)     # keep where fn is True
sorted(lst)         # new sorted list
reversed(lst)       # reversed iterator
any([False,True])   # True
all([True,True])    # True
sum([1,2,3])        # 6
max([1,2,3])        # 3
min([1,2,3])        # 1
abs(-5)             # 5
round(3.14, 1)      # 3.1
pow(2, 10)          # 1024
divmod(10, 3)       # (3, 1)
hash("hello")       # integer hash
id(obj)             # memory address
callable(fn)        # True if callable
repr(obj)           # string representation
chr(65)             # 'A'
ord('A')            # 65
bin(10)             # '0b1010'
oct(10)             # '0o12'
hex(255)            # '0xff'
```

---

## 📌 Collections Module

```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter
c = Counter("abracadabra")
c.most_common(3)     # [('a', 5), ('b', 2), ('r', 2)]
c["a"]               # 5

# defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")   # no KeyError

dd2 = defaultdict(int)
dd2["count"] += 1              # starts at 0

# deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)    # [0, 1, 2, 3]
dq.popleft()        # 0
dq.append(4)        # [1, 2, 3, 4]
dq.pop()            # 4
dq.rotate(1)        # rotate right
deque(lst, maxlen=3) # fixed size queue

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p.x    # 10
p._asdict()        # OrderedDict

# OrderedDict
od = OrderedDict([("a", 1), ("b", 2)])
od.move_to_end("a")
```

---

## 📌 Context Managers

```python
# Using with
with open("file.txt") as f:
    data = f.read()

# Custom class-based
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, *args):
        import time
        print(f"Elapsed: {time.time() - self.start:.2f}s")

with Timer() as t:
    # do something
    pass

# Using contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("setup")
    yield "resource"
    print("teardown")

with managed_resource() as r:
    print(r)
```

---

## 📌 Async / Await

```python
import asyncio

# Coroutine
async def fetch_data(id):
    await asyncio.sleep(1)
    return f"data_{id}"

# Run single coroutine
asyncio.run(fetch_data(1))

# Run multiple concurrently
async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)

asyncio.run(main())

# Async generator
async def ticker(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for val in ticker(5):
        print(val)
```

---

## 📌 Type Hints

```python
from typing import List, Dict, Tuple, Set
from typing import Optional, Union, Any, Callable
from typing import Generator, Iterator, Iterable

def greet(name: str) -> str: ...
def add(a: int, b: int) -> int: ...
def items() -> List[int]: ...
def config() -> Dict[str, Any]: ...
def coords() -> Tuple[float, float]: ...
def find(id: int) -> Optional[str]: ...          # str or None
def handle(x: Union[int, str]) -> None: ...       # int or str

# Python 3.10+ (cleaner)
def find(id: int) -> str | None: ...
def handle(x: int | str) -> None: ...

# Dataclass
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    tags: list = field(default_factory=list)

u = User("Haseeb", 22)
```

---

## 📌 Regular Expressions

```python
import re

text = "Email: dev@gmail.com, Phone: 0312-1234567"

re.search(r'\d+', text)          # first match
re.findall(r'\d+', text)         # all matches list
re.match(r'Email', text)         # match at start only
re.sub(r'\d', '*', text)         # replace
re.split(r',\s*', text)          # split by pattern
re.compile(r'\w+@\w+\.\w+')      # compile for reuse

# Flags
re.IGNORECASE or re.I
re.MULTILINE  or re.M
re.DOTALL     or re.S

# Groups
m = re.search(r'(\w+)@(\w+)\.(\w+)', text)
m.group(0)   # full match
m.group(1)   # first group
m.groups()   # all groups

# Common patterns
r'\d+'        # one or more digits
r'\w+'        # word characters
r'\s+'        # whitespace
r'[a-zA-Z]'  # any letter
r'^start'     # starts with
r'end$'       # ends with
r'.+'         # any char (except newline)
r'.*'         # zero or more any char
```

---

## 📌 Sorting & Searching

```python
lst = [3, 1, 4, 1, 5, 9, 2]

sorted(lst)                        # [1, 1, 2, 3, 4, 5, 9]
sorted(lst, reverse=True)          # descending
lst.sort()                         # in-place
lst.sort(key=lambda x: -x)        # custom key

# Sort objects
users = [{"name": "B", "age": 30}, {"name": "A", "age": 25}]
sorted(users, key=lambda u: u["age"])

# bisect (binary search on sorted list)
import bisect
lst = [1, 3, 5, 7, 9]
bisect.bisect_left(lst, 5)    # 2
bisect.insort(lst, 6)         # insert maintaining order
```

---

## 📌 Functional Tools

```python
from functools import lru_cache, partial, reduce, wraps, cache

# lru_cache (memoization)
@lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

fib.cache_info()   # hits, misses, size
fib.cache_clear()  # clear cache

# cache (Python 3.9+, unlimited)
@cache
def fib(n): ...

# partial (pre-fill arguments)
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
square(5)   # 25
```

---

## 📌 Date & Time

```python
from datetime import datetime, date, time, timedelta
import time as t

# Current time
now = datetime.now()
today = date.today()

# Create
dt = datetime(2024, 1, 15, 10, 30, 0)
d = date(2024, 1, 15)

# Format
now.strftime("%Y-%m-%d %H:%M:%S")   # "2024-01-15 10:30:00"
now.strftime("%d/%m/%Y")             # "15/01/2024"

# Parse
datetime.strptime("2024-01-15", "%Y-%m-%d")

# Arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
diff = datetime(2025, 1, 1) - datetime.now()
diff.days

# Timestamp
t.time()              # Unix timestamp
datetime.fromtimestamp(t.time())
```

---

## 📌 Random Module

```python
import random

random.random()              # float 0.0 to 1.0
random.randint(1, 10)        # int 1 to 10 inclusive
random.randrange(0, 10, 2)   # even numbers 0-8
random.uniform(1.5, 9.5)     # float in range
random.choice([1,2,3,4])     # random element
random.choices([1,2,3], k=5) # k random elements (with replacement)
random.sample([1,2,3,4], 2)  # 2 unique elements
random.shuffle([1,2,3,4])    # shuffle in-place
random.seed(42)              # reproducible results
```

---

## 📌 Comprehension Cheat Sheet

```python
# List
[expr for item in iterable]
[expr for item in iterable if condition]
[expr if condition else other for item in iterable]

# Nested
[x for row in matrix for x in row]

# Dict
{k: v for k, v in pairs}
{k: v for k, v in d.items() if condition}

# Set
{expr for item in iterable}

# Generator
(expr for item in iterable)

# Examples
squares    = [x**2 for x in range(10)]
even_sq    = [x**2 for x in range(10) if x % 2 == 0]
labels     = ["even" if x%2==0 else "odd" for x in range(5)]
word_len   = {w: len(w) for w in ["hi","hello","hey"]}
unique_rem = {x % 5 for x in range(20)}
```

---

## 📌 Useful One-liners

```python
# Swap variables
a, b = b, a

# Flatten nested list
flat = [x for row in matrix for x in row]

# Reverse a string
rev = s[::-1]

# Check palindrome
is_palindrome = s == s[::-1]

# Count vowels
count = sum(1 for c in s if c in "aeiouAEIOU")

# Most frequent element
from collections import Counter
most = Counter(lst).most_common(1)[0][0]

# Remove duplicates keeping order
seen = set()
unique = [x for x in lst if not (x in seen or seen.add(x))]

# Merge two dicts
merged = {**d1, **d2}

# Flatten and unique
flat_unique = list(set(x for row in matrix for x in row))

# Read file lines as list
lines = open("file.txt").read().splitlines()

# Transpose matrix
transposed = list(zip(*matrix))

# All unique
len(lst) == len(set(lst))

# Run shell command
import subprocess
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
```

---

>  Python Cheat Sheet | Save it, use it daily, own it
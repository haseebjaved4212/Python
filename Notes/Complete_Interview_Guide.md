# 🐍 Python Complete Conceptual Interview Guide
> Every concept you need to crack a Python interview — from basics to advanced

---

## 📖 Table of Contents

1. [Python Basics](#1-python-basics)
2. [Data Types](#2-data-types)
3. [Operators](#3-operators)
4. [Control Flow](#4-control-flow)
5. [Functions](#5-functions)
6. [Object-Oriented Programming (OOP)](#6-object-oriented-programming-oop)
7. [Modules and Packages](#7-modules-and-packages)
8. [File Handling](#8-file-handling)
9. [Exception Handling](#9-exception-handling)
10. [Iterators and Generators](#10-iterators-and-generators)
11. [Decorators](#11-decorators)
12. [Comprehensions](#12-comprehensions)
13. [Lambda, Map, Filter, Reduce](#13-lambda-map-filter-reduce)
14. [Collections Module](#14-collections-module)
15. [String Methods](#15-string-methods)
16. [Memory Management and Garbage Collection](#16-memory-management-and-garbage-collection)
17. [Multithreading and Multiprocessing](#17-multithreading-and-multiprocessing)
18. [Async Programming](#18-async-programming)
19. [Context Managers](#19-context-managers)
20. [Regular Expressions](#20-regular-expressions)
21. [Python Internals](#21-python-internals)
22. [Type Hints and Annotations](#22-type-hints-and-annotations)
23. [Design Patterns in Python](#23-design-patterns-in-python)
24. [Testing in Python](#24-testing-in-python)
25. [Top Interview Questions and Answers](#25-top-interview-questions-and-answers)

---

## 1. Python Basics

### What is Python?
Python is a high-level, interpreted, dynamically typed, and garbage-collected programming language. It follows multiple paradigms: procedural, object-oriented, and functional.

### Interpreted vs Compiled
- Python code is **interpreted** line by line at runtime by CPython (the default interpreter)
- It is first compiled to **bytecode** (.pyc files), then interpreted by the Python Virtual Machine (PVM)

### Key Features
- Dynamic typing
- Automatic memory management
- Extensive standard library
- Everything in Python is an **object**

### `__name__ == "__main__"`
```python
if __name__ == "__main__":
    main()
```
This block runs only when the file is executed directly, not when it is imported as a module.

### Python 2 vs Python 3
| Feature | Python 2 | Python 3 |
|---|---|---|
| print | `print "hello"` | `print("hello")` |
| Division | `5/2 = 2` (int) | `5/2 = 2.5` (float) |
| Unicode | ASCII by default | Unicode by default |
| `xrange` | exists | removed (use `range`) |

---

## 2. Data Types

### Built-in Data Types
```
Numeric   → int, float, complex
Text      → str
Boolean   → bool (True / False)
Sequence  → list, tuple, range
Mapping   → dict
Set       → set, frozenset
Binary    → bytes, bytearray
None      → NoneType
```

### Mutable vs Immutable

| Mutable (can change) | Immutable (cannot change) |
|---|---|
| list | int, float, bool |
| dict | str |
| set | tuple |
| bytearray | frozenset, bytes |

```python
# Immutable example
x = "hello"
x[0] = "H"  # TypeError! Strings are immutable

# Mutable example
lst = [1, 2, 3]
lst[0] = 99  # Works fine
```

### List vs Tuple vs Set vs Dict

| | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Ordered | Yes | Yes | No | Yes (Python 3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No |
| Syntax | `[]` | `()` | `{}` | `{k:v}` |

### Type Conversion
```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
list("abc")     # ['a', 'b', 'c']
tuple([1,2,3])  # (1, 2, 3)
set([1,1,2,3])  # {1, 2, 3}
bool(0)         # False
bool(1)         # True
```

### `is` vs `==`
```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b   # True  → same VALUE
a is b   # False → different OBJECT in memory

# is checks identity (same memory address)
# == checks equality (same value)
```

---

## 3. Operators

### Types of Operators
```python
# Arithmetic
+, -, *, /, //, %, **

# Comparison
==, !=, >, <, >=, <=

# Logical
and, or, not

# Bitwise
&, |, ^, ~, <<, >>

# Assignment
=, +=, -=, *=, /=, //=, **=, %=

# Identity
is, is not

# Membership
in, not in
```

### Floor Division vs True Division
```python
10 / 3    # 3.3333 (true division)
10 // 3   # 3      (floor division)
10 % 3    # 1      (modulo / remainder)
2 ** 10   # 1024   (exponentiation)
```

### Ternary Operator
```python
x = 10
result = "even" if x % 2 == 0 else "odd"
```

---

## 4. Control Flow

### if / elif / else
```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

### Loops

```python
# for loop
for i in range(5):
    print(i)

# while loop
x = 0
while x < 5:
    x += 1

# loop with else (runs when loop completes without break)
for i in range(3):
    print(i)
else:
    print("Loop finished")
```

### break, continue, pass
```python
# break - exits the loop
for i in range(10):
    if i == 5:
        break

# continue - skips current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass - placeholder, does nothing
def todo_function():
    pass
```

---

## 5. Functions

### Defining Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Haseeb"))  # Hello, Haseeb!
```

### Default Arguments
```python
def greet(name, msg="Good morning"):
    print(f"{msg}, {name}")

greet("Haseeb")               # Good morning, Haseeb
greet("Haseeb", "Good night") # Good night, Haseeb
```

### *args and **kwargs
```python
# *args → variable number of positional arguments (tuple)
def add(*args):
    return sum(args)

add(1, 2, 3, 4)  # 10

# **kwargs → variable number of keyword arguments (dict)
def show_info(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

show_info(name="Haseeb", role="Developer")
```

### Scope: LEGB Rule
Python resolves names in this order:
1. **L**ocal → inside the current function
2. **E**nclosing → in the enclosing function (for nested functions)
3. **G**lobal → at the module level
4. **B**uilt-in → Python's built-in names like `len`, `print`

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local
    inner()
```

### global and nonlocal
```python
count = 0

def increment():
    global count   # refers to the global variable
    count += 1

def outer():
    x = 10
    def inner():
        nonlocal x  # refers to enclosing scope variable
        x += 1
    inner()
```

### First-Class Functions
Functions in Python are first-class objects. You can assign them to variables, pass them to other functions, and return them.

```python
def square(x):
    return x * x

fn = square      # assign to variable
fn(5)            # 25

def apply(func, value):
    return func(value)

apply(square, 4)  # 16
```

### Closures
A closure is a function that remembers the variables from its enclosing scope even after the outer function has finished.

```python
def multiplier(factor):
    def multiply(number):
        return number * factor  # 'factor' is remembered
    return multiply

double = multiplier(2)
double(5)   # 10
double(10)  # 20
```

---

## 6. Object-Oriented Programming (OOP)

### Class and Object
```python
class Dog:
    species = "Canis lupus"  # class variable (shared)

    def __init__(self, name, age):
        self.name = name     # instance variable
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

d = Dog("Bruno", 3)
print(d.bark())
```

### The 4 Pillars of OOP

#### 1. Encapsulation
Bundling data and methods together, and restricting direct access using access modifiers.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0    # private (name mangling)
        self._owner = "User"  # protected (convention only)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
# acc.__balance  →  AttributeError
acc.get_balance()  # 0 (access via method)
```

Access levels in Python:
| Prefix | Type | Accessible |
|---|---|---|
| `name` | Public | Anywhere |
| `_name` | Protected | Convention only |
| `__name` | Private | Name-mangled to `_ClassName__name` |

#### 2. Inheritance
A child class acquires properties and methods of a parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):       # overriding parent method
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

d = Dog("Bruno")
d.speak()   # Woof!
```

Types of inheritance:
```
Single       → class B(A)
Multiple     → class C(A, B)
Multilevel   → class C(B) where class B(A)
Hierarchical → class B(A), class C(A)
Hybrid       → combination of above
```

#### 3. Polymorphism
Same interface, different behavior depending on the object type.

```python
animals = [Dog("Bruno"), Cat("Whiskers")]

for animal in animals:
    print(animal.speak())  # Woof! then Meow!
```

#### 4. Abstraction
Hiding complex implementation and showing only the essential interface using abstract classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

# Shape()  →  TypeError, cannot instantiate abstract class
c = Circle(5)
c.area()  # 78.5
```

### super()
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # call parent constructor
        self.age = age
```

### MRO - Method Resolution Order
When using multiple inheritance, Python uses C3 linearization to determine which method gets called.

```python
class A:
    def hello(self): print("A")

class B(A):
    def hello(self): print("B")

class C(A):
    def hello(self): print("C")

class D(B, C):
    pass

D().hello()       # B (MRO: D -> B -> C -> A)
print(D.__mro__)  # shows the resolution order
```

### Dunder (Magic) Methods
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):       # print(obj)
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):      # repr(obj), developer-facing
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):  # obj1 + obj2
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):       # len(obj)
        return 2

    def __eq__(self, other): # obj1 == obj2
        return self.x == other.x and self.y == other.y
```

### Class Method vs Static Method vs Instance Method
```python
class MyClass:
    count = 0

    def instance_method(self):      # needs self, accesses instance
        return self

    @classmethod
    def class_method(cls):          # needs cls, accesses class variable
        cls.count += 1
        return cls.count

    @staticmethod
    def static_method(x, y):        # no self or cls, just a utility
        return x + y
```

### Properties (@property)
```python
class Temperature:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):               # getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):        # setter
        if value < -273.15:
            raise ValueError("Too cold!")
        self._celsius = value

    @celsius.deleter
    def celsius(self):               # deleter
        del self._celsius

t = Temperature()
t.celsius = 25   # uses setter
print(t.celsius) # uses getter
```

---

## 7. Modules and Packages

### Importing
```python
import math
import math as m
from math import sqrt, pi
from math import *          # imports everything (not recommended)
```

### Creating a Module
Any `.py` file is a module. You can import it by its filename.

```python
# utils.py
def add(a, b):
    return a + b

# main.py
from utils import add
```

### Package
A package is a directory with an `__init__.py` file.

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

### `__init__.py`
Controls what gets exported when someone does `from package import *` using `__all__`.

```python
# __init__.py
__all__ = ["module1"]
```

---

## 8. File Handling

### Opening Files
```python
# r=read, w=write, a=append, rb=read binary
f = open("file.txt", "r")
content = f.read()
f.close()
```

### Using Context Manager (Recommended)
```python
with open("file.txt", "r") as f:
    content = f.read()     # reads entire file
    lines = f.readlines()  # list of lines
    line = f.readline()    # one line at a time
```

### Writing Files
```python
with open("output.txt", "w") as f:
    f.write("Hello World\n")

with open("output.txt", "a") as f:
    f.write("New line\n")   # append without overwriting
```

### Working with JSON
```python
import json

data = {"name": "Haseeb", "role": "Developer"}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON
with open("data.json", "r") as f:
    loaded = json.load(f)
```

---

## 9. Exception Handling

### try / except / else / finally
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or Value error: {e}")
else:
    print("No error occurred")   # runs only if no exception
finally:
    print("Always runs")         # cleanup code
```

### Raising Exceptions
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Custom Exceptions
```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}.")

raise InsufficientFundsError(500, 200)
```

### Common Built-in Exceptions
```
Exception           → base class
ValueError          → invalid value
TypeError           → wrong type
KeyError            → missing dict key
IndexError          → list index out of range
AttributeError      → object has no attribute
FileNotFoundError   → file does not exist
ZeroDivisionError   → division by zero
ImportError         → module not found
StopIteration       → iterator exhausted
RuntimeError        → general runtime error
OverflowError       → number too large
RecursionError      → max recursion depth exceeded
```

---

## 10. Iterators and Generators

### Iterable vs Iterator
- **Iterable**: any object that can be looped over (list, str, dict, etc.)
- **Iterator**: an object that implements `__iter__()` and `__next__()`

```python
lst = [1, 2, 3]
it = iter(lst)   # creates iterator
next(it)         # 1
next(it)         # 2
next(it)         # 3
next(it)         # StopIteration
```

### Custom Iterator
```python
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for n in Counter(1, 5):
    print(n)  # 1 2 3 4 5
```

### Generators
A generator is a function that uses `yield` instead of `return`. It produces values one at a time, lazily (on demand). Memory-efficient.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
next(gen)  # 5
next(gen)  # 4

# Generator expression (like list comprehension but lazy)
squares = (x**2 for x in range(10))
```

### `yield` vs `return`
| | `return` | `yield` |
|---|---|---|
| Exits function | Yes | No (pauses) |
| Memory | Returns all at once | One value at a time |
| Reusable | No | Yes (resumes state) |

---

## 11. Decorators

### What is a Decorator?
A decorator is a function that takes another function as input and extends or modifies its behavior without changing its source code.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before the function
# Hello!
# After the function
```

### functools.wraps
Preserves the original function's metadata when decorating.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Decorator with Arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()  # prints Hello! 3 times
```

### Class-based Decorator
```python
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"Executed in {time.time() - start:.4f}s")
        return result

@Timer
def slow_function():
    import time
    time.sleep(1)
```

---

## 12. Comprehensions

### List Comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Dict Comprehension
```python
word = "hello"
freq = {char: word.count(char) for char in word}
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### Set Comprehension
```python
unique_squares = {x**2 for x in range(-5, 6)}
```

### Generator Expression
```python
total = sum(x**2 for x in range(100))  # memory efficient
```

### Nested Comprehension
```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 13. Lambda, Map, Filter, Reduce

### Lambda
Anonymous (unnamed) function for short, one-line operations.

```python
square = lambda x: x ** 2
add = lambda x, y: x + y

square(5)   # 25
add(3, 4)   # 7
```

### map()
Applies a function to every element in an iterable.
```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
# [1, 4, 9, 16]
```

### filter()
Filters elements based on a condition (returns only True results).
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4, 6]
```

### reduce()
Reduces a list to a single value by applying a function cumulatively.
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
# 15
```

---

## 14. Collections Module

```python
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
```

### Counter
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
c = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})
c.most_common(2)  # [('apple', 3), ('banana', 2)]
```

### defaultdict
```python
from collections import defaultdict

dd = defaultdict(list)
dd["fruits"].append("apple")    # no KeyError
dd["fruits"].append("banana")
# {'fruits': ['apple', 'banana']}
```

### deque
Double-ended queue. O(1) append/pop from both ends.
```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)   # [0, 1, 2, 3]
dq.popleft()       # 0
dq.rotate(1)       # rotate right
```

### namedtuple
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p.x   # 10
p.y   # 20
```

### OrderedDict
Maintains insertion order (less useful in Python 3.7+ since regular dicts are ordered too).
```python
from collections import OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
```

---

## 15. String Methods

```python
s = "  Hello, World!  "

s.strip()          # "Hello, World!"
s.lower()          # "  hello, world!  "
s.upper()          # "  HELLO, WORLD!  "
s.replace("World", "Python")  # "  Hello, Python!  "
s.split(",")       # ['  Hello', ' World!  ']
",".join(["a","b","c"])  # "a,b,c"
s.startswith("  Hello")  # True
s.endswith("!  ")        # True
s.find("World")    # 9
s.count("l")       # 3
s.isdigit()        # False
s.isalpha()        # False
"42".isdigit()     # True
"abc".isalpha()    # True

# f-strings (Python 3.6+)
name = "Haseeb"
age = 22
f"My name is {name} and I am {age} years old"

# format()
"{} is {} years old".format("Haseeb", 22)

# String slicing
s = "Python"
s[0]     # P
s[-1]    # n
s[1:4]   # yth
s[::-1]  # nohtyP (reverse)
```

---

## 16. Memory Management and Garbage Collection

### How Python Manages Memory
- Python uses **reference counting** as the primary memory management mechanism
- When an object's reference count drops to 0, it is immediately freed
- Python also has a **cyclic garbage collector** to handle reference cycles

```python
import sys
x = [1, 2, 3]
sys.getrefcount(x)  # shows reference count
```

### Reference Counting
```python
a = [1, 2, 3]   # ref count = 1
b = a            # ref count = 2
del a            # ref count = 1
del b            # ref count = 0 → object freed
```

### Garbage Collector
```python
import gc

gc.collect()          # manually trigger GC
gc.get_count()        # (gen0, gen1, gen2) counts
gc.disable()          # disable GC
gc.enable()           # enable GC
```

### Memory Pools (pymalloc)
Python uses its own allocator called **pymalloc** for small objects (< 512 bytes) to avoid calling `malloc` too often.

### `__slots__`
Reduces memory usage by preventing creation of `__dict__` on instances.
```python
class Point:
    __slots__ = ['x', 'y']  # no __dict__ created

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 17. Multithreading and Multiprocessing

### GIL - Global Interpreter Lock
The GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time. This means:
- Threads are good for **I/O-bound** tasks (network, file I/O)
- For **CPU-bound** tasks, use multiprocessing to bypass the GIL

### Threading
```python
import threading

def task(name):
    print(f"Task {name} running")

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()
t1.join()
t2.join()
```

### Thread Synchronization (Lock)
```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1
```

### Multiprocessing
```python
from multiprocessing import Process, Pool

def square(n):
    return n * n

# Multiple processes
p = Process(target=square, args=(5,))
p.start()
p.join()

# Pool for parallel execution
with Pool(4) as pool:
    results = pool.map(square, [1, 2, 3, 4, 5])
```

### Threading vs Multiprocessing
| | Threading | Multiprocessing |
|---|---|---|
| GIL affected | Yes | No |
| Best for | I/O-bound | CPU-bound |
| Memory | Shared | Separate |
| Overhead | Low | Higher |

---

## 18. Async Programming

### asyncio Basics
```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)   # non-blocking sleep
    print(f"Hello, {name}!")

asyncio.run(greet("Haseeb"))
```

### Running Multiple Coroutines
```python
import asyncio

async def task(id, delay):
    await asyncio.sleep(delay)
    print(f"Task {id} done")

async def main():
    await asyncio.gather(
        task(1, 2),
        task(2, 1),
        task(3, 3)
    )

asyncio.run(main())
# Task 2 done → Task 1 done → Task 3 done
```

### async / await Keywords
- `async def` defines a coroutine function
- `await` suspends execution until the awaited task completes
- `asyncio.gather()` runs multiple coroutines concurrently

---

## 19. Context Managers

### Using `with`
```python
with open("file.txt", "r") as f:
    data = f.read()
# file automatically closed after block
```

### Custom Context Manager (class-based)
```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # do not suppress exceptions

with ManagedFile("data.txt") as f:
    print(f.read())
```

### Custom Context Manager (using contextlib)
```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename):
    f = open(filename, "r")
    try:
        yield f
    finally:
        f.close()

with managed_file("data.txt") as f:
    print(f.read())
```

---

## 20. Regular Expressions

```python
import re

text = "My email is haseeb@example.com and phone is 0312-1234567"

# Search
match = re.search(r'\d+', text)   # finds first number

# Find all
numbers = re.findall(r'\d+', text)

# Match (only at beginning of string)
re.match(r'My', text)

# Substitute
clean = re.sub(r'\d', '*', text)   # replace digits with *

# Compile for reuse
pattern = re.compile(r'\w+@\w+\.\w+')
emails = pattern.findall(text)
```

### Common Regex Patterns
```
.     → any character except newline
\d    → digit [0-9]
\w    → word character [a-zA-Z0-9_]
\s    → whitespace
\b    → word boundary
^     → start of string
$     → end of string
*     → 0 or more
+     → 1 or more
?     → 0 or 1
{n}   → exactly n times
{n,m} → between n and m times
[]    → character class
()    → group
|     → or
```

---

## 21. Python Internals

### How Python Executes Code
```
Source Code (.py)
      ↓
Tokenizer/Lexer
      ↓
Parser (AST)
      ↓
Bytecode Compiler (.pyc)
      ↓
Python Virtual Machine (PVM)
      ↓
Output
```

### Interning
Python caches small integers (-5 to 256) and short strings to save memory.
```python
a = 100
b = 100
a is b   # True (interned)

a = 1000
b = 1000
a is b   # False (not interned)
```

### `id()` Function
Returns the memory address of an object.
```python
x = 42
id(x)   # e.g., 140234567891234
```

### Everything is an Object
```python
type(42)         # <class 'int'>
type("hello")    # <class 'str'>
type(print)      # <class 'builtin_function_or_method'>
type(int)        # <class 'type'>
```

### `__dict__`
Most objects store their attributes in a `__dict__` dictionary.
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Haseeb")
p.__dict__   # {'name': 'Haseeb'}
```

### Bytecode Inspection
```python
import dis

def add(a, b):
    return a + b

dis.dis(add)  # shows bytecode instructions
```

---

## 22. Type Hints and Annotations

### Basic Type Hints
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b
```

### Complex Types
```python
from typing import List, Dict, Tuple, Optional, Union, Any

def process(items: List[int]) -> Dict[str, int]:
    return {"total": sum(items)}

def find_user(id: int) -> Optional[str]:  # may return None
    pass

def handle(value: Union[int, str]) -> Any:  # int or str
    pass
```

### Python 3.10+ Style
```python
def greet(name: str | None = None) -> str:
    return f"Hello {name or 'World'}"
```

### Dataclasses
```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"
    tags: list = field(default_factory=list)

p = Point(1.0, 2.0)
print(p)  # Point(x=1.0, y=2.0, label='origin', tags=[])
```

---

## 23. Design Patterns in Python

### Singleton
Only one instance of a class exists.
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
a is b   # True
```

### Factory Pattern
```python
class Dog: pass
class Cat: pass

def animal_factory(animal_type):
    animals = {"dog": Dog, "cat": Cat}
    return animals.get(animal_type)()
```

### Observer Pattern
```python
class EventEmitter:
    def __init__(self):
        self._listeners = []

    def subscribe(self, fn):
        self._listeners.append(fn)

    def emit(self, data):
        for fn in self._listeners:
            fn(data)
```

### Decorator Pattern
Already covered in section 11. Decorators are a Pythonic implementation of the decorator design pattern.

---

## 24. Testing in Python

### unittest
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
```

### pytest (recommended)
```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2
```
Run with: `pytest test_math.py`

### Mocking
```python
from unittest.mock import Mock, patch

mock = Mock()
mock.method.return_value = 42
mock.method()  # 42

with patch("module.function") as mock_fn:
    mock_fn.return_value = "mocked"
```

---

## 25. Top Interview Questions and Answers

**Q1: What is the difference between a list and a tuple?**
Lists are mutable and use `[]`. Tuples are immutable and use `()`. Tuples are faster and can be used as dictionary keys.

**Q2: What is `*args` and `**kwargs`?**
`*args` collects extra positional arguments as a tuple. `**kwargs` collects extra keyword arguments as a dictionary.

**Q3: What is the GIL?**
The Global Interpreter Lock is a mutex in CPython that ensures only one thread runs Python bytecode at a time. It limits true parallelism for CPU-bound tasks but does not affect I/O-bound tasks.

**Q4: What is the difference between `deepcopy` and `copy`?**
```python
import copy

lst = [[1, 2], [3, 4]]
shallow = copy.copy(lst)      # copies outer list, shares inner lists
deep = copy.deepcopy(lst)     # fully independent copy of everything
```

**Q5: What are Python decorators?**
Functions that wrap other functions to extend their behavior without modifying their source code. Used for logging, authentication, timing, caching, etc.

**Q6: What is a generator and why use it?**
A function using `yield` that produces values lazily one at a time. It is memory-efficient since it does not load all values into memory at once.

**Q7: Explain Python's memory management.**
Python uses reference counting and a cyclic garbage collector. Objects are freed when their reference count reaches zero. The GC handles circular references.

**Q8: What is the difference between `@staticmethod` and `@classmethod`?**
`@staticmethod` does not receive `self` or `cls`. It is just a utility function inside a class. `@classmethod` receives `cls` and can access or modify class-level data.

**Q9: What is monkey patching?**
Dynamically modifying a class or module at runtime.
```python
class Dog:
    def bark(self): return "Woof"

Dog.bark = lambda self: "Modified Woof"
```

**Q10: How does Python handle multiple inheritance?**
Using the C3 linearization algorithm (MRO). Use `ClassName.__mro__` to see the resolution order.

**Q11: What is `__slots__`?**
A class-level declaration that restricts instance attributes to a fixed set, reducing memory usage by eliminating the `__dict__` on each instance.

**Q12: What is the difference between `is` and `==`?**
`is` checks identity (same memory address). `==` checks equality (same value).

**Q13: What is a closure?**
A nested function that captures and remembers variables from its enclosing scope even after the outer function has returned.

**Q14: What is `functools.lru_cache`?**
A decorator that caches the result of a function based on its arguments (memoization).
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Q15: What is the difference between `range` and `xrange`?**
`xrange` was Python 2 only and returned a generator. In Python 3, `range` itself is lazy and memory-efficient like `xrange` was.

---

## 📌 Quick Cheat Sheet

```python
# List operations
lst.append(x)     # add to end
lst.insert(i, x)  # insert at index
lst.pop()         # remove last
lst.pop(i)        # remove at index
lst.remove(x)     # remove first occurrence
lst.sort()        # sort in-place
sorted(lst)       # returns new sorted list
lst.reverse()     # reverse in-place
lst[::-1]         # reversed copy

# Dict operations
d.get(key, default)     # safe access
d.keys()                # all keys
d.values()              # all values
d.items()               # key-value pairs
d.update({k: v})        # merge/update
d.pop(key)              # remove key

# Set operations
s.add(x)
s.remove(x)
s.union(s2)        # s | s2
s.intersection(s2) # s & s2
s.difference(s2)   # s - s2
```

---

> Prepared for Python conceptual interviews | Covers Basics to Advanced
> Practice every concept by writing code, not just reading it.
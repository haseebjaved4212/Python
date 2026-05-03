# 🐍 Python Functions — Complete Reference

> Everything you need to know about defining, calling, and mastering functions in Python — from basics to advanced patterns.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-10-orange?style=flat-square)
![Examples](https://img.shields.io/badge/Code%20Examples-30+-purple?style=flat-square)

---

## 📚 Table of Contents

1. [What is a Function?](#1-what-is-a-function)
2. [Anatomy of a Function](#2-anatomy-of-a-function)
3. [Parameters & Arguments](#3-parameters--arguments)
4. [Return Values](#4-return-values)
5. [Scope & Namespaces](#5-scope--namespaces)
6. [Lambda Functions](#6-lambda-functions)
7. [Decorators](#7-decorators)
8. [Generator Functions](#8-generator-functions)
9. [Advanced Patterns](#9-advanced-patterns)
10. [Best Practices](#10-best-practices)

---

## 1. What is a Function?

A function is a **reusable, named block of code** that performs a specific task. You define it once and call it as many times as you need. Functions are the backbone of writing clean, maintainable Python.

They help you:
- Avoid repetition (the **DRY** principle — Don't Repeat Yourself)
- Break big problems into small, manageable pieces
- Make code easier to read, test, and debug

```python
# Without a function — repetitive and hard to maintain
print("Hello, Alice!")
print("Hello, Bob!")
print("Hello, Charlie!")

# With a function — clean, reusable, easy to change
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")
```

---

## 2. Anatomy of a Function

Every function in Python follows this structure. Understanding each part before going deeper is key.

```python
def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: Sum of a and b.
    """
    result = a + b
    return result

# Calling the function
total = add_numbers(10, 20)
print(total)  # 30
```

| Part | Syntax | Purpose | Required? |
|------|--------|---------|-----------|
| Keyword | `def` | Declares a function definition | ✅ Yes |
| Name | `add_numbers` | Identifier used to call the function | ✅ Yes |
| Parameters | `(a, b)` | Inputs the function accepts | ❌ Optional |
| Type hints | `a: int` | Documents expected types (no enforcement) | ❌ Optional |
| Return hint | `-> int` | Documents what type is returned | ❌ Optional |
| Docstring | `"""..."""` | Human-readable description | ❌ Optional |
| Body | indented block | The actual code that runs | ✅ Yes |
| Return | `return result` | Sends a value back to the caller | ❌ Optional |

---

## 3. Parameters & Arguments

Python gives you a lot of flexibility in how you pass data into functions. There are five distinct ways.

### 3.1 Positional Parameters

```python
def describe(name, age):
    print(f"{name} is {age} years old")

describe("Haseeb", 25)   # order matters here
```

### 3.2 Default Parameter Values

```python
def power(base, exponent=2):   # exponent defaults to 2
    return base ** exponent

print(power(3))      # 9  — uses default
print(power(3, 3))   # 27 — overrides default
```

> [!WARNING]
> **Common gotcha:** Never use mutable objects (lists, dicts) as default parameter values. They are created once at function definition time, not each call. Use `None` and initialize inside the body instead.

```python
# BAD — the list is shared across all calls!
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad("a"))   # ['a']
print(add_item_bad("b"))   # ['a', 'b']  <-- unexpected!

# GOOD — fresh list every call
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 3.3 Keyword Arguments

```python
def connect(host, port, timeout):
    print(f"Connecting to {host}:{port} (timeout={timeout}s)")

# Named — order doesn't matter
connect(timeout=30, host="localhost", port=5432)
```

### 3.4 `*args` — Variable Positional Arguments

Collects any number of positional arguments into a **tuple**.

```python
def total(*numbers):   # numbers is a tuple
    return sum(numbers)

print(total(1, 2, 3))           # 6
print(total(10, 20, 30, 40))    # 100
```

### 3.5 `**kwargs` — Variable Keyword Arguments

Collects any number of keyword arguments into a **dict**.

```python
def build_profile(**info):   # info is a dict
    for key, value in info.items():
        print(f"  {key}: {value}")

build_profile(name="Haseeb", role="dev", lang="Python")
```

### 3.6 Combining All Parameter Types

The correct order when mixing all types:

```python
def func(positional_only, /, normal, *args, keyword_only, **kwargs):
    pass
```

> [!TIP]
> Python enforces this order strictly. Positional-only params go before `/`, keyword-only params go after `*args`.

---

## 4. Return Values

Functions can return any Python object. If no `return` statement is present (or just `return` alone), Python implicitly returns `None`.

```python
# Return a single value
def square(n):
    return n ** 2

# Return multiple values (Python packs them into a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 4, 7])
print(low, high)   # 1 9

# Early return — guard clause pattern
def divide(a, b):
    if b == 0:
        return None   # exit early, skip the rest
    return a / b
```

---

## 5. Scope & Namespaces

Python resolves variable names using the **LEGB** rule:

```
Local → Enclosing → Global → Built-in
```

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local

    inner()
    print(x)       # enclosing

outer()
print(x)           # global
```

### Modifying Variables from Outer Scopes

```python
# Modify a global variable inside a function
counter = 0

def increment():
    global counter
    counter += 1

# Modify an enclosing variable from a nested function
def make_counter():
    count = 0

    def tick():
        nonlocal count
        count += 1
        return count

    return tick

counter_fn = make_counter()
print(counter_fn())   # 1
print(counter_fn())   # 2
```

> [!WARNING]
> Avoid `global` as much as possible. It makes functions hard to test and reason about. Pass values as parameters and return results instead.

---

## 6. Lambda Functions

A lambda is a small, **anonymous** function defined in a single expression. It cannot contain statements or multiple lines. Best used as a short throwaway passed to another function.

```python
# Syntax: lambda params: expression
double = lambda x: x * 2
add    = lambda a, b: a + b

# Common use: sorting with a custom key
students = [("Alice", 88), ("Bob", 95), ("Carol", 72)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)   # [('Bob', 95), ('Alice', 88), ('Carol', 72)]

# With map() and filter()
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))      # [1, 4, 9, 16, 25]
evens   = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
```

> [!WARNING]
> If your lambda is getting complex or you need to reuse it — write a proper `def` function. Lambdas are for quick, single-use cases only.

---

## 7. Decorators

A decorator is a function that **wraps another function** to extend or modify its behavior, without changing the original source code. One of the most powerful patterns in Python.

### Building a Decorator from Scratch

```python
import functools
import time

def timer(func):
    """Decorator that prints how long a function takes."""
    @functools.wraps(func)   # preserves original func metadata
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} ran in {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_task():
    time.sleep(0.5)
    print("Task done")

slow_task()
# Task done
# slow_task ran in 0.5002s
```

### Decorator with Arguments

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()   # prints Hi! three times
```

### Common Built-in Decorators

| Decorator | Where | Purpose |
|-----------|-------|---------|
| `@staticmethod` | Classes | Method that doesn't need `self` or `cls` |
| `@classmethod` | Classes | Method that receives the class as first arg |
| `@property` | Classes | Access a method like an attribute |
| `@functools.lru_cache` | Anywhere | Cache return values for repeated calls |
| `@functools.wraps` | Inside decorators | Preserve wrapped function's metadata |

---

## 8. Generator Functions

A generator uses `yield` instead of `return`. It produces values **one at a time** and pauses between each one, making it extremely memory-efficient for large datasets.

```python
# Regular function — builds the entire list in memory at once
def get_squares_list(n):
    return [x**2 for x in range(n)]

# Generator — yields one value at a time, uses almost no memory
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

gen = get_squares_gen(1_000_000)
print(next(gen))   # 0
print(next(gen))   # 1

# Use in a for loop just like any iterable
for sq in get_squares_gen(5):
    print(sq)   # 0 1 4 9 16
```

### Generator Expression (one-liner)

```python
# Similar to list comprehension but lazy
squares_gen = (x**2 for x in range(10))
print(sum(squares_gen))   # 285
```

> [!TIP]
> Use generators when working with large files, database rows, API pagination, or any scenario where loading everything into memory at once is not practical.

---

## 9. Advanced Patterns

### 9.1 Closures

A closure is a function that **remembers variables from its enclosing scope**, even after that scope has finished executing.

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor   # 'factor' is captured from outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))   # 20
print(triple(10))   # 30
```

### 9.2 Higher-Order Functions

Functions that take other functions as arguments or return them as results.

```python
def apply_twice(func, value):
    return func(func(value))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))   # 20
```

### 9.3 Recursive Functions

A function that calls itself. Always needs a **base case** to stop, otherwise you hit infinite recursion.

```python
def factorial(n):
    if n <= 1:               # base case — stops recursion
        return 1
    return n * factorial(n - 1)   # recursive call

print(factorial(5))   # 120 → 5 * 4 * 3 * 2 * 1
```

### 9.4 Memoization with `lru_cache`

Cache expensive function results automatically. Huge performance win for repeated calls with the same arguments.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))   # instant — no redundant computation
```

### 9.5 Partial Functions

Fix some arguments of a function and create a new, simpler one.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

print(square(5))   # 25
print(cube(3))     # 27
```

---

## 10. Best Practices

| Practice | Why it Matters |
|----------|----------------|
| **One function, one job** | Easier to test, debug, and reuse. If you can't describe it in one sentence, split it. |
| **Use descriptive names** | `calculate_tax()` beats `ct()` every time. Code is read more than it is written. |
| **Write docstrings** | Documents purpose, args, and return value. `help()` and IDEs use them. |
| **Add type hints** | Makes intent clear, enables static analysis with `mypy`, improves autocomplete. |
| **Keep functions short** | Aim for under 20 lines. If it scrolls, it probably does too much. |
| **Avoid side effects** | Pure functions (same input = same output, no state changes) are predictable and testable. |
| **Use guard clauses** | Return early for edge cases to avoid deep nesting. Flat code is easier to follow. |
| **Never use mutable defaults** | Default `[]` or `{}` are shared across calls. Use `None` instead. |

### Putting It All Together

```python
from typing import Optional

def calculate_discount(
    price: float,
    discount_pct: float,
    max_discount: Optional[float] = None
) -> float:
    """
    Calculate discounted price with an optional cap.

    Args:
        price:         Original price in USD.
        discount_pct:  Discount percentage (0-100).
        max_discount:  Maximum discount amount allowed. No cap if None.

    Returns:
        Final price after discount is applied, rounded to 2 decimal places.

    Raises:
        ValueError: If price is negative.
    """
    if price < 0:
        raise ValueError("Price cannot be negative")

    discount = price * (discount_pct / 100)

    if max_discount is not None:
        discount = min(discount, max_discount)

    return round(price - discount, 2)


# Usage
print(calculate_discount(100, 20))           # 80.0
print(calculate_discount(100, 50, max_discount=30))  # 70.0
```

---

## Quick Reference Cheat Sheet

```python
# Basic function
def func(param): ...

# With defaults
def func(param=default): ...

# Variable args
def func(*args, **kwargs): ...

# Type hints
def func(x: int, y: str = "hi") -> bool: ...

# Lambda
fn = lambda x: x * 2

# Decorator
@decorator
def func(): ...

# Generator
def gen():
    yield value

# Recursive
def rec(n):
    if base_case: return result
    return rec(n - 1)

# Cached
from functools import lru_cache
@lru_cache(maxsize=None)
def func(n): ...
```

---

<div align="center">

**Python Functions Reference** — Made with 💚 by Haseeb

*Python 3.10+ · Feel free to fork and star ⭐*

</div>
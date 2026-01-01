# Variables in Python — Detailed Guide

This document explains variables in Python: how they work, naming rules, assignment patterns, scoping, typing, and best practices with examples.

## What is a variable?
- A variable is a name that refers to an object/value in memory. In Python variables are references (bindings), not typed containers.

## Naming rules and conventions
- Names can contain letters, digits, and underscores, but cannot start with a digit.
- Names are case-sensitive: `value`, `Value`, and `VALUE` are different.
- Follow PEP 8 style: use `lower_case_with_underscores` for variable names.
- Avoid Python built-in names (e.g., `list`, `dict`, `str`) as variable names.

Valid examples:

```python
user_id = 42
first_name = "Ada"
_temp = None
```

## Assignment
- Use the assignment operator `=` to bind a name to an object.
- Python uses dynamic typing: the same variable can be rebound to objects of different types.

```python
x = 10        # x refers to int(10)
print(x)
x = "ten"   # now x refers to str("ten")
```

## Multiple assignment and unpacking
- Assign multiple variables at once: `a, b = 1, 2`.
- Unpack iterables: `first, *rest = [1,2,3,4]`.

```python
a, b = 1, 2
coords = (10, 20)
x, y = coords
names = ["A","B","C"]
head, *tail = names
```

## Mutable vs Immutable objects
- Variables hold references. Mutating an object (like a `list`) affects all references to it.
- Immutable objects (like `int`, `str`, `tuple`) cannot be changed in-place; rebinding creates a new object.

```python
lst1 = [1, 2]
lst2 = lst1
lst2.append(3)
print(lst1)  # [1, 2, 3] — both names reference the same list

num1 = 5
num2 = num1
num2 = num2 + 1
print(num1)  # 5 — ints are immutable, num2 was rebound
```

## Types and type hints
- Python is dynamically typed, but you can add optional static hints using the `typing` module.

```python
from typing import List
count: int = 10
names: List[str] = ["Ada", "Grace"]
```

Type hints are for tooling and readability; they do not change runtime behavior.

## Casting / conversion
- Use built-in constructors to convert types: `int()`, `str()`, `float()`, `bool()`, `list()`.

```python
value = "42"
number = int(value)  # 42
```

## Constants
- Python has no true constants; by convention, use ALL_CAPS names for values that shouldn’t change.

```python
MAX_RETRIES = 5
```

## Variable scope: local, global, nonlocal
- Local variables: declared inside functions; lifetime is the function call.
- Global variables: module-level variables accessible throughout the module.
- Use `global` to rebind a module-level name from inside a function (use sparingly).
- Use `nonlocal` to rebind a variable from an enclosing (but not global) scope in nested functions.

```python
COUNTER = 0

def increment():
	global COUNTER
	COUNTER += 1

def outer():
	x = 0
	def inner():
		nonlocal x
		x += 1
	inner()
	return x
```

## Common pitfalls
- Mutable default arguments: avoid `def f(x, cache={}):` — use `None` and create inside the function.
- Shadowing built-ins or outer variables can cause confusing bugs.
- Relying on implicit type conversions can produce unexpected results.

Bad example (mutable default):

```python
def append_item(item, lst=[]):
	lst.append(item)
	return lst

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2]  <-- shared default list
```

Fix:

```python
def append_item(item, lst=None):
	if lst is None:
		lst = []
	lst.append(item)
	return lst
```

## Best practices
- Use clear, descriptive variable names.
- Prefer small scopes and avoid excessive use of globals.
- Use constants (ALL_CAPS) for fixed configuration values.
- Add type hints where they improve readability and static checking.
- Keep mutable state explicit and minimize shared mutable objects.

## Quick reference
- Assign: `name = value`
- Multiple: `a, b = 1, 2`
- Unpack: `first, *rest = iterable`
- Type hint: `var: int = 0`
- Constant: `MY_CONST = 3.14`

## Further reading
- PEP 8 — Style Guide for Python Code
- PEP 484 — Type Hints
- Official Python tutorial: Variables and Types

---



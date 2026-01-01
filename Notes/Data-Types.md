# Data Types in Python — Detailed Guide

This document describes Python's core data types, how they behave, operations you can perform on them, mutability, type checking, conversions, and best practices.

## Overview

- Python provides a rich set of built-in data types. Variables are references to objects; objects have types.
- Types covered here: numeric types, boolean, strings & bytes, sequences (list, tuple, range), sets, mappings (dict), None, and callable types.

### Python Data Type Hierarchy

```
object
├── None
├── bool (subtype of int)
├── int
├── float
├── complex
├── str
├── bytes
├── bytearray
├── list
├── tuple
├── range
├── set
├── frozenset
├── dict
└── [custom classes, callables, etc.]
```

## Numeric types

- `int`: arbitrary-precision integers.
- `float`: double-precision floating point numbers.
- `complex`: complex numbers with real and imaginary parts (`a + bj`).

Examples:

```python
n: int = 42
f: float = 3.14
c: complex = 1 + 2j
```

Operations: `+ - * / // % **` and math functions from `math` or `cmath`.

## Boolean

- `bool` is a subtype of `int`. Values: `True`, `False`.
- Truthiness: many objects have truth value semantics (e.g., empty collections are `False`).

```python
is_valid = True
if not []:  # empty list is False
    pass
```

## Text and bytes

- `str`: immutable Unicode text. Use string methods (`.split()`, `.join()`, `.format()`, f-strings).
- `bytes`: immutable sequences of bytes; `bytearray` is a mutable variant.

```python
s = "Hello, world"
b = b"binary\x00data"
```

## Sequences: list, tuple, range

- `list`: mutable, ordered sequence. Supports append, extend, insert, pop, remove, slicing, iteration.
- `tuple`: immutable ordered sequence. Use for fixed collections or keys in dicts.
- `range`: immutable sequence of numbers, memory-efficient for iteration.

```python
lst = [1, 2, 3]
lst.append(4)
T = (10, 20)
for i in range(0, 10, 2):
    pass
```

Indexing and slicing work for sequences: `seq[start:stop:step]`.

### Sequence Structure Diagram

```
list:  [0] → 1   [1] → 2   [2] → 3   [3] → 4
       Index: 0        1         2         3

tuple: (0) → 10  (1) → 20
       Index: 0        1

Slicing example: lst[1:3] → [2, 3]
                 lst[::2] → [1, 3]  (every 2nd element)
```

## Sets

- `set`: unordered collection of unique, hashable items; supports `add`, `remove`, set operations (`|, &, -, ^`).
- `frozenset`: immutable set.

### Set Operations Diagram

```
s1 = {1, 2, 3}
s2 = {3, 4, 5}

Union (|):        s1 | s2  → {1, 2, 3, 4, 5}
                  ┌─────────────────────┐
                  │ 1, 2, 3, 4, 5       │
                  └─────────────────────┘

Intersection (&): s1 & s2  → {3}
                  ┌─────────────────────┐
                  │         3           │
                  └─────────────────────┘

Difference (-):   s1 - s2  → {1, 2}
                  ┌─────────────────────┐
                  │ 1, 2                │
                  └─────────────────────┘

Symmetric Diff(^): s1 ^ s2 → {1, 2, 4, 5}
                  ┌─────────────────────┐
                  │ 1, 2, 4, 5          │
                  └─────────────────────┘
```

```python
s = {1, 2, 3}
s.add(4)
union = s | {5, 6}
```

## Mappings: dict

- `dict`: key → value mapping. Keys must be hashable.
- Common operations: indexing `d[key]`, `get`, `setdefault`, `pop`, `.keys()`, `.values()`, `.items()`.

### Dictionary Structure Diagram

```
dict = {"name": "Alice", "age": 30, "city": "NYC"}

┌─────────────────────────────────────────┐
│ Key → Value Pairs (Hash Table)          │
├────────┬──────────────────────────────┤
│ "name" → "Alice"                       │
│ "age"  → 30                            │
│ "city" → "NYC"                         │
└────────┴──────────────────────────────┘

Access: d["name"] → "Alice"
        d.get("age") → 30
        d.get("zip", None) → None (safe)
```

```python
d = {"a": 1, "b": 2}
value = d.get("c", 0)
for k, v in d.items():
    pass
```

## None

- `None` is a singleton used to denote absence of a value.

```python
result = None
if result is None:
    pass
```

## Mutability and identity

- Mutable objects (e.g., `list`, `dict`, `set`, `bytearray`) can be changed in-place.
- Immutable objects (e.g., `int`, `str`, `tuple`, `frozenset`) cannot be changed; operations produce new objects.
- `is` checks identity; `==` checks equality.

### Mutable vs Immutable Diagram

```
MUTABLE (can be changed in-place):
┌─────────────────────────────────┐
│ list, dict, set, bytearray      │
│ Changes affect all references   │
│ Example: lst = [1,2]            │
│          ref2 = lst             │
│          ref2.append(3)         │
│          lst → [1,2,3] ✓        │
└─────────────────────────────────┘

IMMUTABLE (cannot be changed in-place):
┌─────────────────────────────────┐
│ int, float, str, tuple, bool    │
│ Operations create new objects   │
│ Example: x = 42                 │
│          y = x                  │
│          y = y + 1    (y → 43)  │
│          x still 42   ✓        │
└─────────────────────────────────┘
```

```python
a = [1, 2]
b = a
b.append(3)
assert a is b
assert a == [1, 2, 3]

x = 1000
y = 1000
print(x is y)  # implementation-dependent
```

## Copying objects

- Shallow copy: use `list.copy()` or `copy.copy()` for top-level copies.
- Deep copy: use `copy.deepcopy()` to recursively copy nested mutables.

### Shallow vs Deep Copy Diagram

```
Original:   orig = [[1, 2], [3, 4]]
            ┌──────────┬──────────┐
            │   ↓      │    ↓     │
            │ [1, 2]   │  [3, 4]  │
            └──────────┴──────────┘

Shallow Copy: sh = orig.copy()
            ┌──────────┬──────────┐
            │   ↓      │    ↓     │
            │ [1, 2]   │  [3, 4]  │  ← Same inner lists!
            └──────────┴──────────┘
            sh[0].append(99) → orig also changes

Deep Copy:  dp = copy.deepcopy(orig)
            ┌──────────┬──────────┐
            │   ↓      │    ↓     │
            │ [1, 2]   │  [3, 4]  │  ← Different inner lists
            └──────────┴──────────┘
            dp[0].append(99) → orig unchanged
```

```python
import copy
orig = [[1], [2]]
sh = orig.copy()
dp = copy.deepcopy(orig)
```

## Type checking and introspection

- `type(obj)` returns the object's type.
- `isinstance(obj, Type)` is preferred for type checks.
- Use `dir()`, `help()`, and `__class__` for introspection.

```python
if isinstance(x, (int, float)):
    pass
```

## Type hints (optional static typing)

- Use `typing` for annotations: `List`, `Dict`, `Tuple`, `Optional`, `Union`, `Any`.
- Type hints improve readability and help linters/IDE tooling; they don't change runtime types.

```python
from typing import List, Dict, Optional
names: List[str] = ["A", "B"]
def lookup(key: str) -> Optional[int]:
    return None
```

## Common conversions

- `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()` (constructor conversions).

### Type Conversion Diagram

```
From ↓ To →   int        float       str         bool
─────────────────────────────────────────────────────
int    ✓       "42"→42   42→42.0     42→"42"     42→True
float  3.14→3  ✓         3.14→3.14   3.14→"3.14" 3.14→True
str    "42"→42 "3.14"→3  ✓           "42"→"42"   "42"→True
list   ✗       ✗         [1]→"[1]"   [1]→True
dict   ✗       ✗         {..}→"{..}" {..}→True
None   ✗       ✗         None→"None" None→False
```

```python
num = int("42")
text = str(3.14)
chars = list("abc")
```

## Literals and constructors

- Numeric: `42`, `3.14`, `1+2j`.
- String: `'text'`, `"text"`, triple-quoted for multi-line.
- List/tuple/set/dict literals: `[1,2]`, `(1,2)`, `{1,2}`, `{"k": "v"}`.

## Operations summary

- Arithmetic on numbers, concatenation for sequences (`+`), repetition (`*`), membership (`in`), length `len()`.

```python
len([1,2,3])
"a" in "abc"
[1,2] + [3]
```

## Best practices

- Choose the correct data type for the problem (e.g., `tuple` for fixed records, `list` for mutateable sequences).
- Prefer immutability when possible to avoid shared-state bugs.
- Use comprehensions (`[x*x for x in xs]`, `{k:v for ...}`, `{x for x in xs}`) for clarity and performance.
- Use type hints for public APIs and complex code.
- Validate assumptions when parsing external data (e.g., JSON) and cast to expected types.

## Performance notes

- `list` is efficient for indexed access and append/pop from end; `deque` from `collections` is better for FIFO operations.
- `set` and `dict` provide average O(1) membership and lookup.

## Examples

```python
# sequence unpacking
head, *middle, tail = [1,2,3,4,5]

# dict comprehension
squares = {n: n*n for n in range(6)}

# set operations
s1 = {1,2,3}
s2 = {3,4,5}
common = s1 & s2
```

## Further reading

- Official Python Docs — Built-in Types
- PEP 8 — Style Guide for Python Code
- PEP 484 — Type Hints

---



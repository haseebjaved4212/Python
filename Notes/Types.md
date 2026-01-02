# Type Conversion in Python — Detailed Guide

## Overview

This document explains Python type conversion (casting), covering implicit and explicit conversions, common built-in conversion functions, pitfalls, and practical examples. It is meant for beginners through intermediate Python users.

## Table of Contents

- Overview
- Implicit vs Explicit Conversion
- Built-in conversion functions
- Numeric conversions and bases
- Sequence & mapping conversions
- Bytes and strings
- Boolean conversion rules
- Common errors and how to handle them
- Best practices
- Examples you can run

## Implicit vs Explicit Conversion

- Implicit conversion: Python automatically converts one data type to another (e.g., int to float in arithmetic). This is safe and lossless in typical cases.

Example:

```py
>>> 3 + 2.5
5.5
```

- Explicit conversion (casting): You manually convert types using functions like `int()`, `float()`, `str()`, etc. Use this when you need a specific type or when Python won't convert automatically.

Example:

```py
>>> int('42')
42
```

## Built-in conversion functions

- `int(x, base=10)`: Convert `x` to integer. If `x` is a string, you can provide a numeric base (2, 8, 10, 16, ...).
- `float(x)`: Convert `x` to floating-point number.
- `str(x)`: Convert `x` to string.
- `bool(x)`: Convert `x` to boolean (`False` for zero, empty collections, `None`, `False`; otherwise `True`).
- `complex(x, y=0)`: Construct a complex number.
- `list(x)`, `tuple(x)`, `set(x)`: Convert iterable `x` to respective sequence/collection.
- `dict(x)`: Convert mapping or iterable of key/value pairs to `dict`.
- `bytes(s, encoding)` / `bytearray(...)`: Build bytes objects.
- `ord(char)` / `chr(int)`: Convert between characters and their Unicode code points.
- `hex(int)`, `bin(int)`, `oct(int)`: Get hexadecimal, binary, octal string representations.

## Numeric conversions and bases

- Converting a string with a prefix or base:

```py
>>> int('0b1010', 0)   # base=0 auto-detects prefix
10
>>> int('FF', 16)
255
>>> int('1010', 2)
10
```

- Beware of floating point precision when converting floats:

```py
>>> float(1)/3
0.3333333333333333
```

## Sequence & mapping conversions

- Convert between lists/tuples/sets:

```py
>>> list((1,2,3))
[1, 2, 3]
>>> tuple([1,2,3])
(1, 2, 3)
>>> set([1,2,2,3])
{1, 2, 3}
```

- Convert an iterable of pairs to a dict:

```py
>>> dict([('a', 1), ('b', 2)])
{'a': 1, 'b': 2}
```

- Convert a dict to lists of keys/values:

```py
>>> d = {'x':1, 'y':2}
>>> list(d.keys())
['x', 'y']
>>> list(d.values())
[1, 2]
```

## Bytes and strings

- To convert string to bytes: `s.encode(encoding='utf-8')`.
- To convert bytes to string: `b.decode(encoding='utf-8')`.

```py
>>> s = 'hello'
>>> b = s.encode('utf-8')
>>> b
b'hello'
>>> b.decode('utf-8')
'hello'
```

- When converting numbers to bytes, consider `int.to_bytes()` and `int.from_bytes()` for precise control.

## Boolean conversion rules

The following convert to `False` with `bool()`:

- `None`
- `False`
- Zero of any numeric type: `0`, `0.0`, `0j`
- Empty sequences/collections: `''`, `[]`, `()`, `{}`, `set()`, `range(0)`
  Everything else is `True`.

```py
>>> bool('')
False
>>> bool([0])
True
>>> bool(0)
False
```

## Common errors and handling

- `ValueError` when converting a non-numeric string to `int()`/`float()`:

```py
int('abc')  # ValueError
```

- `TypeError` when the input type isn't supported by the conversion function:

```py
int([1,2,3])  # TypeError
```

Use `try/except` or pre-validate with helper checks:

```py
def to_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None
```

## Best practices

- Prefer explicit conversion for clarity.
- Validate input before casting, or handle exceptions.
- Use `str.format()` or `f-strings` for safe string interpolation of converted values.
- For bulk conversions, use list comprehensions or generator expressions instead of `map()` when readability matters.
- When converting from user input (e.g., `input()`), always sanitize/validate.

## Examples you can run

Here are runnable examples. Save them to a `.py` file and run with `python`.

Example: convert list of numeric strings to ints and filter invalid entries

```py
data = ['10', '20', 'x', '30']
ints = []
for s in data:
    try:
        ints.append(int(s))
    except ValueError:
        pass

print(ints)  # [10, 20, 30]
```

Using list comprehension with `try/except` via a helper:

```py
def safe_int(s):
    try:
        return int(s)
    except Exception:
        return None

converted = [safe_int(x) for x in data]
filtered = [x for x in converted if x is not None]
print(filtered)
```

Convert comma-separated numbers from user input to floats:

```py
s = '1.2, 3.4, 5.6'
nums = [float(x.strip()) for x in s.split(',')]
print(nums)
```

Bytes and encodings example:

```py
text = 'café'
b = text.encode('utf-8')
print(b)
print(b.decode('utf-8'))
```

Complex numbers:

```py
>>> complex('1+2j')
(1+2j)
>>> complex(3)  # 3 + 0j
(3+0j)
```

## Quick reference table

- `int(x)` — string/number -> int (may raise ValueError)
- `float(x)` — string/number -> float
- `str(x)` — any -> string
- `bool(x)` — any -> True/False rules
- `list(x)`, `tuple(x)`, `set(x)` — convert iterable types
- `dict(x)` — mapping or iterable-of-pairs -> dict
- `s.encode()` / `b.decode()` — str <-> bytes

## Troubleshooting tips

- If `int(s)` raises `ValueError`, print the string repr to inspect whitespace or hidden characters: `print(repr(s))`.
- For non-ASCII text, always specify encoding when moving between bytes and str.
- When converting floats to ints, remember `int()` truncates toward zero, not round.

## Further reading

- Official docs: https://docs.python.org/3/library/functions.html (see `int`, `float`, `str`, `bytes`)

---

If you'd like, I can:

- add runnable example files under `Code/` and link them, or
- adapt this README to match `Code/05_Types.py` examples.
# Operators in Python — Detailed Guide

This document covers Python operators: arithmetic, comparison, logical, bitwise, assignment, identity, membership, and their precedence with examples.

## Overview

- **Operators** are special symbols that perform operations on operands (values/variables).
- Python operators are classified by category: arithmetic, comparison, logical, bitwise, assignment, identity, and membership.
- **Operator precedence** determines the order of evaluation in complex expressions.

## Arithmetic Operators

Perform mathematical operations on numeric types.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division (float) | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Arithmetic Operators Diagram

```
Addition:      5 + 3 = 8
               ┌────────────┐
               │ 5 + 3 = 8  │
               └────────────┘

Division types:
    /  (float division):    10 / 3 = 3.333...
    // (floor division):    10 // 3 = 3
    %  (modulus):           10 % 3 = 1

Exponentiation:  2 ** 3 = 2 × 2 × 2 = 8
```

Examples:

```python
result = 5 + 3
quotient = 10 // 3
remainder = 10 % 3
power = 2 ** 5
```

## Comparison Operators

Compare two values and return `True` or `False`.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 3` | `True` |

### Comparison Operators Diagram

```
        5 == 5  →  True   (Equal)
        5 != 3  →  True   (Not Equal)
    
    Number line:
    ... 3 ------- 5 -------  10 ...
    
        5 > 3   →  True   (5 is to the right)
        5 < 10  →  True   (5 is to the left)
        5 <= 5  →  True   (Equal or less)
        5 >= 5  →  True   (Equal or greater)
```

Examples:

```python
if x == 5:
    pass
if age >= 18:
    print("Adult")
while count < 10:
    count += 1
```

## Logical Operators

Combine boolean expressions using logic (AND, OR, NOT).

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Both conditions true | `True and True` | `True` |
| `or` | At least one true | `True or False` | `True` |
| `not` | Negates boolean | `not False` | `True` |

### Logical Operators Truth Table

```
AND Truth Table:
┌─────────┬─────────┬───────────┐
│ Left    │ Right   │ Result    │
├─────────┼─────────┼───────────┤
│ True    │ True    │ True      │
│ True    │ False   │ False     │
│ False   │ True    │ False     │
│ False   │ False   │ False     │
└─────────┴─────────┴───────────┘

OR Truth Table:
┌─────────┬─────────┬───────────┐
│ Left    │ Right   │ Result    │
├─────────┼─────────┼───────────┤
│ True    │ True    │ True      │
│ True    │ False   │ True      │
│ False   │ True    │ True      │
│ False   │ False   │ False     │
└─────────┴─────────┴───────────┘

NOT Truth Table:
┌─────────┬───────────┐
│ Value   │ Result    │
├─────────┼───────────┤
│ True    │ False     │
│ False   │ True      │
└─────────┴───────────┘
```

Examples:

```python
if age >= 18 and has_license:
    print("Can drive")
if x < 0 or x > 100:
    print("Out of range")
if not is_empty:
    process()
```

## Bitwise Operators

Operate on binary representations of integers.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `5 >> 1` | `2` |

### Bitwise Operators Diagram

```
Binary representations:
    5 = 0101
    3 = 0011

AND (&):      0101
              0011
              ────
              0001 = 1

OR (|):       0101
              0011
              ────
              0111 = 7

XOR (^):      0101
              0011
              ────
              0110 = 6

NOT (~):      ~0101 = 1010 (inverts all bits)

Left Shift (<<):   0101 << 1 = 1010 (shift left, add 0)
                   Equivalent to multiply by 2

Right Shift (>>):  0101 >> 1 = 0010 (shift right, drop last)
                   Equivalent to divide by 2
```

Examples:

```python
a = 5  # binary: 0101
b = 3  # binary: 0011
result = a & b  # 1
result = a | b  # 7
result = a ^ b  # 6
```

## Assignment Operators

Assign values to variables; combined with other operators for shorthand.

| Operator | Example | Equivalent |
|----------|---------|------------|
| `=` | `x = 5` | Direct assignment |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `\|=` | `x \|= 3` | `x = x \| 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `<<=` | `x <<= 1` | `x = x << 1` |
| `>>=` | `x >>= 1` | `x = x >> 1` |

### Assignment Operators Shorthand

```
Original:       count = count + 1
Shorthand:      count += 1

Original:       total = total * 2
Shorthand:      total *= 2

Original:       value = value % 10
Shorthand:      value %= 10
```

Examples:

```python
count = 0
count += 1      # count is now 1
count *= 2      # count is now 2
text = "Hello"
text += " World"  # text is now "Hello World"
```

## Identity Operators

Check if two variables refer to the same object (memory address).

| Operator | Description | Example |
|----------|-------------|---------|
| `is` | Same object (identity) | `x is y` |
| `is not` | Different object | `x is not y` |

### Identity vs Equality Diagram

```
Equality (==):   Checks if VALUES are the same
    a = [1, 2]
    b = [1, 2]
    a == b  →  True   (same values)

Identity (is):   Checks if they're the SAME object
    a = [1, 2]
    b = [1, 2]
    a is b  →  False  (different objects)
    
    c = a
    c is a  →  True   (same object reference)
```

Examples:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different objects)

c = a
print(c is a)  # True (same reference)

if x is None:  # Correct way to check None
    pass
```

## Membership Operators

Check if a value exists in a sequence.

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Value in sequence | `x in list` |
| `not in` | Value not in sequence | `x not in list` |

### Membership Operators Diagram

```
List: [1, 2, 3, 4, 5]
    
    3 in [1,2,3,4,5]      →  True
    10 in [1,2,3,4,5]     →  False
    
    3 not in [1,2,3,4,5]  →  False
    10 not in [1,2,3,4,5] →  True

String: "Hello"
    
    "H" in "Hello"        →  True
    "x" in "Hello"        →  False
```

Examples:

```python
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("Found")

fruits = ["apple", "banana", "orange"]
if "grape" not in fruits:
    fruits.append("grape")
```

## Operator Precedence

Operators are evaluated in a specific order. Higher precedence operators are evaluated first.

### Operator Precedence Table (Highest to Lowest)

```
Priority  Operator                  Description
─────────────────────────────────────────────────────
1         ()                        Parentheses
2         **                        Exponentiation
3         +x, -x, ~x                Unary plus, minus, bitwise NOT
4         *, /, //, %               Multiplication, division, floor division, modulus
5         +, -                      Addition, subtraction
6         <<, >>                    Bitwise shifts
7         &                         Bitwise AND
8         ^                         Bitwise XOR
9         |                         Bitwise OR
10        ==, !=, <, >, <=, >=      Comparisons
11        is, is not                Identity
12        in, not in                Membership
13        not                       Logical NOT
14        and                       Logical AND
15        or                        Logical OR
```

### Precedence Examples

```
Without parentheses:     2 + 3 * 4  =  14  (multiply first)
With parentheses:        (2 + 3) * 4 = 20  (add first)

Complex:    2 ** 3 * 4 + 5  =  8 * 4 + 5  =  32 + 5  =  37
             ↑ exponent first
                    ↑ multiply second
                           ↑ add last

Logic:      True and False or True  =  False or True  =  True
             ↑ 'and' before 'or'
```

Examples:

```python
result = 2 + 3 * 4      # 14 (multiplication first)
result = (2 + 3) * 4    # 20 (parentheses change order)
result = 2 ** 3 * 2     # 16 (exponent before multiply)
if a > 5 and b < 10 or c == 0:  # 'and' before 'or'
    pass
```

## String Operators

Special uses of operators with strings.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Concatenation | `"Hello" + " World"` → `"Hello World"` |
| `*` | Repetition | `"Ha" * 3` → `"HaHaHa"` |

Examples:

```python
greeting = "Hello" + " " + "World"
repeated = "-" * 10  # "----------"
pattern = "ab" * 3   # "ababab"
```

## Operator Chaining

Compare multiple values in one expression.

```python
if 0 < x < 10:          # Equivalent to: 0 < x and x < 10
    print("In range")

if a == b == c:         # All three equal
    pass

if a < b < c < d:       # Ascending order
    pass
```

## Common Pitfalls

### 1. Confusing `=` (assignment) with `==` (comparison)
```python
# Wrong (assignment, not comparison)
if x = 5:
    pass

# Correct
if x == 5:
    pass
```

### 2. Using `is` for value comparison
```python
# Wrong (identity, not equality)
if x is 5:
    pass

# Correct (for value comparison)
if x == 5:
    pass
```

### 3. Operator precedence surprises
```python
# Wrong
result = 2 ** 3 ** 2  # 512 (right-associative: 2**(3**2))

# Clarify with parentheses
result = 2 ** (3 ** 2)  # 512
result = (2 ** 3) ** 2  # 64
```

## Best Practices

- **Use parentheses** for clarity, even when not strictly required.
- **Choose the right operator**: `==` for values, `is` for identity checks.
- **Be aware of precedence**: Use parentheses to avoid mistakes.
- **Avoid chaining assignments**: `x = y = z = 0` works but can be confusing.
- **Use compound operators** (`+=`, `-=`, etc.) for readability.
- **Short-circuit evaluation**: `and`/`or` stop early when result is determined.

## Quick Reference

```python
# Arithmetic
x + y, x - y, x * y, x / y, x // y, x % y, x ** y

# Comparison
x == y, x != y, x < y, x > y, x <= y, x >= y

# Logical
x and y, x or y, not x

# Bitwise
x & y, x | y, x ^ y, ~x, x << y, x >> y

# Assignment
x = y, x += y, x -= y, x *= y, x /= y

# Identity
x is y, x is not y

# Membership
x in y, x not in y

# String
"a" + "b", "x" * 3

# Precedence: () > ** > unary > *, /, //, % > +, - > << >> > & > ^ > | > comparison > is > in > not > and > or
```

## Examples and Exercises

### Example: Calculating Average

```python
scores = [85, 90, 78, 92, 88]
average = sum(scores) / len(scores)
if average >= 80:
    print("Good average")
```

### Example: Checking Valid Age Range

```python
age = 25
if 18 <= age < 65:
    print("Working age")
```

### Example: Bitwise Flag Check

```python
flags = 0b1101  # binary: 1101
if flags & 0b0100:  # Check if bit 2 is set
    print("Flag is set")
```

---

Created as a comprehensive reference on Python operators. Suggest edits or ask for more examples!

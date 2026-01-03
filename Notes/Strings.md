# Strings in Python

In Python, a string is a sequence of characters. It is an immutable data type, which means that once a string is created, it cannot be changed. Strings are used to represent text-based data, such as names, sentences, and file paths.

## Creating Strings

You can create strings in Python using single quotes (`'`), double quotes (`""`), or triple quotes (```""" """``` or ```''' '''```).

```python
# Single-quoted string
single_quoted_string = 'Hello, World!'

# Double-quoted string
double_quoted_string = "Hello, World!"

# Triple-quoted string (can span multiple lines)
triple_quoted_string = """This is a multi-line
string in Python."""
```

## String Indexing and Slicing

Strings can be indexed and sliced to access individual characters or substrings.

- **Indexing:** Access a single character at a specific position. Python uses 0-based indexing.
- **Slicing:** Access a range of characters.

```python
my_string = "Python is fun"

# Indexing
print(my_string[0])   # Output: 'P'
print(my_string[-1])  # Output: 'n' (negative indexing from the end)

# Slicing
print(my_string[0:6])  # Output: 'Python' (characters from index 0 to 5)
print(my_string[7:])   # Output: 'is fun' (from index 7 to the end)
print(my_string[:6])   # Output: 'Python' (from the beginning to index 5)
print(my_string[:])    # Output: 'Python is fun' (the entire string)
```

## String Methods

Python provides a rich set of built-in methods for string manipulation. Here are some of the most common ones:

| Method          | Description                                                    |
|-----------------|----------------------------------------------------------------|
| `upper()`       | Converts the string to uppercase.                              |
| `lower()`       | Converts the string to lowercase.                              |
| `strip()`       | Removes leading and trailing whitespace.                       |
| `lstrip()`      | Removes leading whitespace.                                    |
| `rstrip()`      | Removes trailing whitespace.                                   |
| `replace(old, new)` | Replaces all occurrences of `old` with `new`.                  |
| `split(separator)` | Splits the string into a list of substrings at the separator. |
| `startswith(prefix)` | Returns `True` if the string starts with the `prefix`.       |
| `endswith(suffix)`   | Returns `True` if the string ends with the `suffix`.         |
| `find(substring)` | Returns the lowest index of the substring. Returns -1 if not found. |
| `count(substring)` | Returns the number of occurrences of the substring.          |

**Example:**

```python
text = "   Hello, Python!   "

print(text.upper())         # Output: "   HELLO, PYTHON!   "
print(text.lower())         # Output: "   hello, python!   "
print(text.strip())         # Output: "Hello, Python!"
print(text.replace("Python", "World")) # Output: "   Hello, World!   "
print(text.strip().split(',')) # Output: ['Hello', ' Python!']
```

## String Concatenation and Formatting

You can combine strings using the `+` operator or format them to embed variables.

### Concatenation

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

### Formatting

#### f-Strings (Formatted String Literals)

Introduced in Python 3.6, f-strings are the most modern and preferred way to format strings.

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.
```

#### `str.format()` Method

This method is available in older Python versions.

```python
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Bob and I am 25 years old.

print("My name is {n} and I am {a} years old.".format(n=name, a=age))
# Output: My name is Bob and I am 25 years old.
```

## Escape Sequences

Escape sequences are special character combinations that are used to represent non-printable characters or characters that have a special meaning in strings.

| Sequence | Description        |
|----------|--------------------|
| `\n`     | Newline            |
| `\t`     | Tab                |
| `\\`     | Backslash          |
| `\'`     | Single quote       |
| `\"`     | Double quote       |

**Example:**

```python
print("This is a line.\nThis is a new line.")
print("This is a single quote: '\'")
print("This is a double quote: \"")
print("This is a backslash: \\")
```

## Raw Strings

If you want to prevent escape sequences from being interpreted, you can use raw strings by prefixing the string literal with an `r` or `R`.

```python
# Regular string
print("C:\new\folder")
# Output:
# C:\
# ew\folder

# Raw string
print(r"C:\new\folder")
# Output: C:\new\folder
```

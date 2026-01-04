

# Lists in Python — The Ultimate Guide

Mastery of Python lists. A list is an ordered, mutable collection that can hold any Python object type. This guide covers creation, common operations, slicing, comprehensions, and best practices.

## 1. The basics

Creating a list uses square brackets:

```python
fruits = ["Apple", "Banana", "Cherry"]
mixed = [42, "Rocket", 3.14, True]
```

Accessing items (zero-based indexing):

- First item: `fruits[0]`
- Last item: `fruits[-1]`

## 2. Core operations

Common methods and their typical use:

| Method             | Complexity | Best for                                      |
| ------------------ | ---------: | --------------------------------------------- |
| `append(x)`        |       O(1) | Adding a single item at the end               |
| `extend(iterable)` |       O(k) | Merging another iterable into the list        |
| `insert(i, x)`     |       O(n) | Inserting at a specific index (use sparingly) |

Removing items:

```python
item = my_list.pop()        # Removes and returns last item (O(1))
my_list.remove("Apple")    # Removes first matching value (O(n))
my_list.clear()             # Removes all items
```

## 3. Slicing

Use slicing to extract sublists: `list[start:stop:step]`.

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])   # [1, 2, 3]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4]
print(nums[::-1])  # [5, 4, 3, 2, 1, 0]
```

## 4. List comprehensions

Comprehensions provide concise, readable list creation.

```python
# Instead of building incrementally:
squares = []
for x in range(10):
    squares.append(x**2)

# Use a comprehension:
squares = [x**2 for x in range(10) if x % 2 == 0]
```

## 5. Best practices

1. Performance pitfall

   - Avoid inserting/removing at the beginning of a list (`list.insert(0, x)` or `list.pop(0)`) — these are O(n). If you need fast operations at both ends, use `collections.deque`.

2. Checking emptiness

   - Prefer truthiness over length checks:

```python
if not my_list:
    print("The list is empty")
```

3. Copying lists

   - `list_b = list_a` creates a reference. To copy:

```python
list_b = list_a.copy()
# or
list_b = list_a[:]
```

## Summary checklist

- [x] Use `append()` for adding single items efficiently.
- [x] Use slicing for sub-sections.
- [x] Use list comprehensions for concise readable code.
- [x] Use `deque` for frequent head operations.

Happy coding — remember indexes start at 0!



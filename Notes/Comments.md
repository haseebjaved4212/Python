# Comments in Python

This file covers how to write and use comments in Python source code.

## What are comments?

- Comments are non-executed text in source code used to explain intent, rationale, or notes for maintainers.

## Single-line comments

- Use `#` to start a comment that runs to the end of the line.

Example:

```python
# This is a single-line comment
print("Hello")  # Inline comment explaining this print
```

## Multi-line comments and docstrings

- Triple-quoted strings (""" or ''' ) are often used for multi-line comments or documentation strings (docstrings).
- Docstrings placed immediately after a module, class, or function definition are accessible at runtime via `__doc__`.

Example:

```python
def greet(name):
	"""Return a greeting for `name`.

	Docstrings should describe the function's behavior, parameters, and return value.
	"""
	return f"Hello, {name}!"
```

## Inline comments

- Keep inline comments short and place them on the same line after at least two spaces.
- Prefer explaining _why_ something is done, not _what_ the code obviously does.

## Best practices

- Write comments to explain intent, algorithmic choices, or non-obvious side effects.
- Keep comments up to date; stale comments are worse than none.
- Use docstrings for public APIs (modules, classes, functions).
- Avoid commenting trivial code; instead, make code self-explanatory when possible.

## Commenting-out code

- Temporarily disabling code with comments is fine during development, but remove unused blocks before committing.

## Quick reference

- Single-line: `# comment`
- Multi-line/docstring: `"""multi-line"""` or `'''multi-line'''`

## Examples

```python
# Good: explains why, not what
result = complex_calculation(x)  # result used for caching strategy

def compute():
	"""Compute important metric used in reporting."""
	pass
```


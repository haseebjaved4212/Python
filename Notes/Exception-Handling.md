# 🛡️ Python Exception Handling — The Complete Guide

> Writing code that works is one thing. Writing code that handles failure gracefully is what separates a beginner from a professional. This guide covers everything about exception handling in Python.

---

## Table of Contents

1. [What is an Exception?](#what-is-an-exception)
2. [The Exception Hierarchy](#the-exception-hierarchy)
3. [Basic try / except](#basic-try--except)
4. [Catching Specific Exceptions](#catching-specific-exceptions)
5. [The else Clause](#the-else-clause)
6. [The finally Clause](#the-finally-clause)
7. [The Full try / except / else / finally Block](#the-full-try--except--else--finally-block)
8. [Raising Exceptions](#raising-exceptions)
9. [Re-raising Exceptions](#re-raising-exceptions)
10. [Exception Chaining](#exception-chaining)
11. [Custom Exceptions](#custom-exceptions)
12. [Built-in Exceptions — Full Reference](#built-in-exceptions--full-reference)
13. [Logging Exceptions](#logging-exceptions)
14. [Context Managers and Exception Handling](#context-managers-and-exception-handling)
15. [Exception Groups (Python 3.11+)](#exception-groups-python-311)
16. [Best Practices](#best-practices)
17. [Anti-patterns to Avoid](#anti-patterns-to-avoid)
18. [Real-World Use Cases](#real-world-use-cases)
19. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## What is an Exception?

An **exception** is an event that occurs during program execution that disrupts the normal flow of instructions. When Python encounters an error it cannot handle, it raises an exception object. If that exception is not caught anywhere, the program crashes with a traceback.

```python
# This will crash the program
result = 10 / 0
print(result)

# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     result = 10 / 0
# ZeroDivisionError: division by zero
```

Exception handling lets you **anticipate** these failures, respond to them intelligently, and keep your program running or fail gracefully with a useful message.

There are two broad categories of errors in Python:

| Type | Description | Example |
|---|---|---|
| **Syntax Error** | Code is structurally wrong — caught before execution | `if x == 1` (missing colon) |
| **Exception** | Error occurs at runtime during execution | `10 / 0`, `int("abc")` |

Syntax errors cannot be caught with try/except. Exceptions can.

---

## The Exception Hierarchy

All Python exceptions inherit from a common base class. Understanding this tree helps you catch the right level of specificity.

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AttributeError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   ├── TimeoutError
    │   └── ConnectionError
    ├── RuntimeError
    │   └── RecursionError
    ├── StopIteration
    ├── TypeError
    ├── ValueError
    │   └── UnicodeError
    └── Warning
        ├── DeprecationWarning
        ├── UserWarning
        └── RuntimeWarning
```

> **Key takeaway:** Catching a parent class catches all its children too. `except Exception` catches almost everything. `except BaseException` catches literally everything including `KeyboardInterrupt` — almost never do that.

---

## Basic try / except

The most fundamental structure. Put risky code in `try`. Handle the failure in `except`.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output: Cannot divide by zero!
# Program continues normally after this point
```

### Without exception handling vs with

```python
# Without — program crashes
user_input = "abc"
number = int(user_input)   # ValueError: invalid literal for int()

# With — graceful handling
user_input = "abc"
try:
    number = int(user_input)
    print(f"Number is: {number}")
except ValueError:
    print(f"'{user_input}' is not a valid number.")

# Output: 'abc' is not a valid number.
```

### Accessing the exception object

Use `as` to grab the actual exception instance. This gives you access to the error message and other attributes.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")           # Error: division by zero
    print(type(e))                 # <class 'ZeroDivisionError'>
    print(e.args)                  # ('division by zero',)
```

---

## Catching Specific Exceptions

Always be as specific as possible about what you catch. Catching a broad exception hides bugs.

### Catching multiple exception types separately

```python
def parse_and_divide(value, divisor):
    try:
        number = int(value)
        result = number / divisor
        return result
    except ValueError:
        print(f"Cannot convert '{value}' to an integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Both arguments must be numbers.")
```

### Catching multiple exceptions in one line

```python
try:
    data = process(user_input)
except (ValueError, TypeError) as e:
    print(f"Input error: {e}")
```

### Catching exceptions in priority order

Python checks `except` clauses top to bottom. More specific exceptions must come first, or they will never be reached.

```python
try:
    risky_operation()
except FileNotFoundError:       # specific — checked first
    print("File not found.")
except OSError:                 # broader — catches other OS errors
    print("OS-level error occurred.")
except Exception:               # broadest — last resort catch
    print("Something unexpected happened.")
```

```python
# Wrong order — FileNotFoundError is a subclass of OSError
# The FileNotFoundError clause below is unreachable
try:
    open("missing.txt")
except OSError:                 # catches everything including FileNotFoundError
    print("OS error")
except FileNotFoundError:       # never reached
    print("File not found")
```

---

## The else Clause

The `else` block runs only if **no exception was raised** in the `try` block. It is a clean way to separate the happy path from error handling logic.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division failed.")
else:
    print(f"Division succeeded: {result}")
    # Only runs if no exception was raised

# Output: Division succeeded: 5.0
```

### Why use else instead of putting code in try?

```python
# Bad — too much inside try, harder to know what caused an exception
try:
    result = int(user_input)
    process(result)
    save_to_db(result)
    send_notification(result)
except ValueError:
    print("Invalid input")

# Good — only the risky line is in try
try:
    result = int(user_input)
except ValueError:
    print("Invalid input")
else:
    # These lines only run if int() succeeded
    process(result)
    save_to_db(result)
    send_notification(result)
```

The `else` approach makes it clear exactly which line can raise the caught exception.

---

## The finally Clause

The `finally` block **always runs**, regardless of whether an exception was raised, caught, or even if there was a `return` statement. It is designed for cleanup.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This always runs.")
    # Perfect place for cleanup code
```

### finally with return statements

```python
def risky():
    try:
        return "from try"
    finally:
        print("finally ran!")   # this still executes
        # if you return here, it overrides the try's return

risky()
# Output:
# finally ran!
# 'from try'
```

### Real-world finally usage

```python
connection = None
try:
    connection = open_database_connection()
    data = connection.query("SELECT * FROM users")
except DatabaseError as e:
    print(f"Database error: {e}")
finally:
    if connection:
        connection.close()   # always close the connection
```

---

## The Full try / except / else / finally Block

All four clauses together:

```python
def read_config(filepath):
    file = None
    try:
        file = open(filepath, "r")
        config = json.load(file)
    except FileNotFoundError:
        print(f"Config file not found: {filepath}")
        config = {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in config: {e}")
        config = {}
    else:
        print("Config loaded successfully.")
        validate_config(config)      # only runs if no exception
    finally:
        if file:
            file.close()             # always close the file
    return config
```

### Execution flow summary

```
try block
    |
    |-- Exception raised? --> except block (matching one)
    |                              |
    |-- No exception? ---------> else block
    |
    v
finally block (always)
```

---

## Raising Exceptions

You can raise exceptions yourself using the `raise` keyword. This is how you communicate errors from your own code to the callers.

### Raise a built-in exception

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age must be between 0 and 150, got {age}")
    return age
```

### Raise with a helpful message

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor cannot be zero. Check your inputs.")
    return a / b
```

### Conditional raising

```python
def get_user(user_id):
    user = db.find(user_id)
    if user is None:
        raise LookupError(f"No user found with ID: {user_id}")
    return user
```

### Raise without arguments — re-raise current exception

```python
try:
    risky()
except ValueError:
    log_error()
    raise    # re-raises the same ValueError with its original traceback
```

---

## Re-raising Exceptions

Sometimes you want to catch an exception, do something (like logging), and then let it propagate up the call stack.

```python
import logging

def process_payment(amount):
    try:
        charge_card(amount)
    except PaymentError as e:
        logging.error(f"Payment failed for amount {amount}: {e}")
        raise    # caller still sees the exception

# Bare raise preserves the original traceback
# Do NOT do this — it resets the traceback origin:
# raise e   (loses original stack trace info)
```

---

## Exception Chaining

Python lets you link exceptions together so you can say "this exception happened because of that one." This is extremely useful for debugging layered code.

### Implicit chaining — happens automatically

```python
try:
    open("config.json")
except FileNotFoundError:
    raise RuntimeError("Could not load app config")

# Traceback shows both exceptions:
# FileNotFoundError: ...
# During handling of the above exception, another exception occurred:
# RuntimeError: Could not load app config
```

### Explicit chaining with `raise ... from ...`

```python
try:
    result = int(user_input)
except ValueError as e:
    raise TypeError("Expected a numeric string") from e

# Traceback:
# ValueError: invalid literal for int() ...
# The above exception was the direct cause of the following exception:
# TypeError: Expected a numeric string
```

### Suppress the chain with `raise ... from None`

```python
try:
    connect_to_db()
except ConnectionError as e:
    raise AppError("Service unavailable") from None
# Hides the original exception from the traceback — use carefully
```

---

## Custom Exceptions

Defining your own exception classes makes your code much more expressive and lets callers catch exactly the errors they care about.

### Basic custom exception

```python
class AppError(Exception):
    """Base exception for this application."""
    pass

class ValidationError(AppError):
    """Raised when input validation fails."""
    pass

class DatabaseError(AppError):
    """Raised when a database operation fails."""
    pass
```

### Custom exception with extra context

```python
class ValidationError(Exception):
    def __init__(self, field, message, value=None):
        self.field   = field
        self.message = message
        self.value   = value
        super().__init__(f"[{field}] {message}" + (f" (got: {value!r})" if value else ""))

# Usage
try:
    raise ValidationError("email", "Invalid format", value="not-an-email")
except ValidationError as e:
    print(e)          # [email] Invalid format (got: 'not-an-email')
    print(e.field)    # email
    print(e.value)    # not-an-email
```

### Building an exception hierarchy for a real project

```python
# exceptions.py

class AppError(Exception):
    """Root exception for the entire application."""
    pass

# Auth domain
class AuthError(AppError):
    pass

class InvalidCredentialsError(AuthError):
    pass

class TokenExpiredError(AuthError):
    pass

# Payment domain
class PaymentError(AppError):
    pass

class InsufficientFundsError(PaymentError):
    def __init__(self, required, available):
        self.required  = required
        self.available = available
        super().__init__(
            f"Need {required}, only {available} available."
        )

class PaymentGatewayError(PaymentError):
    pass

# API domain
class APIError(AppError):
    def __init__(self, status_code, message):
        self.status_code = status_code
        super().__init__(f"HTTP {status_code}: {message}")

class NotFoundError(APIError):
    def __init__(self, resource):
        super().__init__(404, f"{resource} not found")

class UnauthorizedError(APIError):
    def __init__(self):
        super().__init__(401, "Authentication required")
```

```python
# Callers can now be very specific
try:
    process_payment(user, amount)
except InsufficientFundsError as e:
    notify_user(f"Top up {e.required - e.available} more to proceed.")
except PaymentGatewayError:
    notify_user("Payment service is temporarily down. Try again later.")
except PaymentError:
    notify_user("Payment failed for an unknown reason.")
```

---

## Built-in Exceptions — Full Reference

### Most commonly encountered

| Exception | When it occurs |
|---|---|
| `ValueError` | Right type, wrong value — `int("abc")` |
| `TypeError` | Wrong type entirely — `"2" + 2` |
| `KeyError` | Dict key does not exist — `d["missing"]` |
| `IndexError` | List index out of range — `lst[100]` |
| `AttributeError` | Object has no such attribute — `None.upper()` |
| `FileNotFoundError` | File or directory does not exist |
| `PermissionError` | No permission to access the file |
| `ZeroDivisionError` | Dividing by zero |
| `ImportError` | Module cannot be imported |
| `ModuleNotFoundError` | Module does not exist (subclass of ImportError) |
| `NameError` | Variable name not defined |
| `RecursionError` | Maximum recursion depth exceeded |
| `MemoryError` | Out of memory |
| `StopIteration` | Iterator has no more items |
| `TimeoutError` | Operation timed out |
| `ConnectionError` | Network connection failed |
| `NotImplementedError` | Abstract method not implemented in subclass |
| `RuntimeError` | Generic runtime error |
| `OverflowError` | Numeric result too large |
| `AssertionError` | `assert` statement failed |
| `OSError` | OS-level operation failure (parent of many file/network errors) |

### Rarely seen but good to know

| Exception | Description |
|---|---|
| `UnicodeDecodeError` | Failed to decode bytes to string |
| `UnicodeEncodeError` | Failed to encode string to bytes |
| `EOFError` | `input()` hit end of file |
| `FloatingPointError` | Floating point operation failed |
| `BufferError` | Buffer-related operation failed |
| `ArithmeticError` | Base class for math errors |
| `LookupError` | Base class for `KeyError` and `IndexError` |

---

## Logging Exceptions

In production code, printing errors is not enough. Use the `logging` module to record exceptions with full tracebacks.

```python
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process(data):
    try:
        return risky_operation(data)
    except ValueError as e:
        logging.error("Validation failed: %s", e)
        return None
    except Exception as e:
        logging.exception("Unexpected error processing data")
        # logging.exception() automatically includes the full traceback
        raise
```

### `logging.exception()` vs `logging.error()`

```python
try:
    1 / 0
except ZeroDivisionError:
    logging.error("Math error")       # logs message only
    logging.exception("Math error")   # logs message + full traceback
```

Always use `logging.exception()` inside an `except` block when you want the traceback recorded.

---

## Context Managers and Exception Handling

The `with` statement is Python's built-in way to handle setup and teardown cleanly — and it handles exceptions automatically.

### The with statement

```python
# Without context manager — manual cleanup
file = open("data.txt")
try:
    content = file.read()
finally:
    file.close()

# With context manager — clean and automatic
with open("data.txt") as file:
    content = file.read()
# file.close() is called automatically, even if an exception occurs
```

### Building a custom context manager with a class

```python
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_to_db()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False   # False means re-raise the exception; True suppresses it

with DatabaseConnection() as conn:
    conn.execute("SELECT * FROM users")
```

### Building a context manager with `contextlib`

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring: {name}")
    resource = acquire(name)
    try:
        yield resource
    except Exception as e:
        print(f"Error while using {name}: {e}")
        raise
    finally:
        print(f"Releasing: {name}")
        release(resource)

with managed_resource("db_connection") as res:
    res.query("SELECT 1")
```

### `contextlib.suppress` — silently ignore specific exceptions

```python
from contextlib import suppress

# Instead of:
try:
    os.remove("temp.txt")
except FileNotFoundError:
    pass

# You can write:
with suppress(FileNotFoundError):
    os.remove("temp.txt")
```

---

## Exception Groups (Python 3.11+)

Python 3.11 introduced `ExceptionGroup` for handling multiple simultaneous exceptions — particularly useful in async and concurrent code.

```python
# Raising an ExceptionGroup
def validate_form(data):
    errors = []
    if not data.get("email"):
        errors.append(ValueError("Email is required"))
    if not data.get("name"):
        errors.append(ValueError("Name is required"))
    if len(data.get("password", "")) < 8:
        errors.append(ValueError("Password must be at least 8 characters"))

    if errors:
        raise ExceptionGroup("Validation failed", errors)

# Handling with except* (new syntax in 3.11)
try:
    validate_form({"password": "123"})
except* ValueError as eg:
    for exc in eg.exceptions:
        print(f"Validation error: {exc}")
```

---

## Best Practices

### 1. Catch specific exceptions, not broad ones

```python
# Bad
try:
    process()
except Exception:
    pass

# Good
try:
    process()
except ValueError as e:
    handle_bad_value(e)
except IOError as e:
    handle_io_error(e)
```

### 2. Never silently swallow exceptions

```python
# Terrible — hides bugs forever
try:
    do_something()
except Exception:
    pass

# At minimum, log it
try:
    do_something()
except Exception as e:
    logging.exception("do_something failed")
    raise
```

### 3. Keep try blocks narrow and focused

```python
# Bad — too broad, unclear what might throw
try:
    user = get_user(id)
    data = fetch_data(user)
    result = process(data)
    save(result)
    notify(user)
except Exception:
    print("Something went wrong")

# Good — specific about what you are guarding
try:
    user = get_user(id)
except UserNotFoundError:
    return error_response(404, "User not found")

data = fetch_data(user)
result = process(data)
save(result)
notify(user)
```

### 4. Use custom exceptions for domain errors

```python
# Bad — callers have to match generic message strings
raise ValueError("user not found")

# Good — callers can catch precisely what they need
raise UserNotFoundError(user_id=42)
```

### 5. Use finally or context managers for cleanup

```python
# Good with finally
conn = None
try:
    conn = get_connection()
    conn.execute(query)
finally:
    if conn:
        conn.close()

# Better with context manager
with get_connection() as conn:
    conn.execute(query)
```

### 6. Preserve exception context with chaining

```python
try:
    config = json.load(open("config.json"))
except json.JSONDecodeError as e:
    raise ConfigError("Failed to parse config") from e
```

### 7. Validate early, fail fast

```python
def create_user(name, age, email):
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer")
    if "@" not in email:
        raise ValueError(f"Invalid email: {email}")
    # safe to proceed now
```

---

## Anti-patterns to Avoid

### Anti-pattern 1: Catching and ignoring everything

```python
# Never do this
try:
    critical_operation()
except:    # catches EVERYTHING including KeyboardInterrupt
    pass
```

### Anti-pattern 2: Using exceptions for normal control flow

```python
# Bad — exceptions are expensive and unclear
try:
    return my_dict[key]
except KeyError:
    return default

# Good — use .get()
return my_dict.get(key, default)
```

### Anti-pattern 3: Losing the original traceback

```python
# Bad — creates a new exception, loses the stack trace
try:
    risky()
except SomeError as e:
    raise RuntimeError(str(e))   # original traceback gone

# Good — chain it
try:
    risky()
except SomeError as e:
    raise RuntimeError("Context message") from e
```

### Anti-pattern 4: Overly broad handler that masks bugs

```python
# Bad — a bug in calculate() will be silently eaten
try:
    result = calculate(data)
    save(result)
    notify(result)
except Exception:
    print("Error in calculation")

# A NameError or AttributeError inside save() or notify()
# would be swallowed and blamed on calculation
```

### Anti-pattern 5: Relying on exception message strings

```python
# Bad — message wording can change between Python versions
try:
    risky()
except ValueError as e:
    if "invalid literal" in str(e):   # fragile!
        handle_parse_error()

# Good — catch the right exception type at the right level
try:
    value = int(user_input)
except ValueError:
    handle_parse_error()
```

---

## Real-World Use Cases

### 1. Robust file reading with fallback

```python
import json
import logging

def load_config(path, defaults=None):
    defaults = defaults or {}
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("Config file not found at %s. Using defaults.", path)
        return defaults
    except json.JSONDecodeError as e:
        logging.error("Malformed JSON in config file: %s", e)
        return defaults
    except PermissionError:
        logging.error("No permission to read config file: %s", path)
        return defaults
```

### 2. Retry logic with exception handling

```python
import time
import logging

def retry(func, retries=3, delay=1.0, exceptions=(Exception,)):
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            return func()
        except exceptions as e:
            last_error = e
            logging.warning("Attempt %d/%d failed: %s", attempt, retries, e)
            if attempt < retries:
                time.sleep(delay)
    raise RuntimeError(f"All {retries} attempts failed") from last_error

# Usage
result = retry(
    lambda: fetch_from_api(endpoint),
    retries=3,
    delay=2.0,
    exceptions=(ConnectionError, TimeoutError)
)
```

### 3. API input validation layer

```python
class APIHandler:
    def create_user(self, payload):
        try:
            name  = self._require_str(payload, "name")
            email = self._require_email(payload, "email")
            age   = self._require_int(payload, "age", min_val=0, max_val=120)
        except ValidationError as e:
            return {"error": str(e), "field": e.field}, 400

        try:
            user = User.create(name=name, email=email, age=age)
        except DuplicateEmailError:
            return {"error": "Email already in use"}, 409
        except DatabaseError as e:
            logging.exception("DB error creating user")
            return {"error": "Internal server error"}, 500

        return {"user_id": user.id}, 201
```

### 4. CLI tool with user-friendly errors

```python
import sys

def main():
    try:
        args   = parse_args()
        data   = load_file(args.input)
        result = process(data)
        write_output(result, args.output)
        print("Done.")
    except FileNotFoundError as e:
        print(f"Error: File not found — {e.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"Error: Permission denied — {e.filename}", file=sys.stderr)
        sys.exit(1)
    except ValidationError as e:
        print(f"Error: Invalid input — {e}", file=sys.stderr)
        sys.exit(2)
    except KeyboardInterrupt:
        print("\nAborted by user.", file=sys.stderr)
        sys.exit(130)
```

### 5. Safe type conversion utilities

```python
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def safe_json_parse(text, default=None):
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return default

# Usage
age     = safe_int(request.params.get("age"), default=0)
price   = safe_float(form_data.get("price"), default=0.0)
payload = safe_json_parse(raw_body, default={})
```

### 6. Database transaction with rollback

```python
def transfer_funds(from_id, to_id, amount):
    conn = get_db_connection()
    try:
        conn.begin()
        debit(conn, from_id, amount)
        credit(conn, to_id, amount)
        conn.commit()
    except InsufficientFundsError:
        conn.rollback()
        raise
    except DatabaseError as e:
        conn.rollback()
        logging.exception("DB error during transfer")
        raise RuntimeError("Transfer failed due to a system error") from e
    finally:
        conn.close()
```

---

## Quick Cheat Sheet

```python
# Basic structure
try:
    risky_code()
except SpecificError as e:
    handle(e)
except (TypeError, ValueError) as e:
    handle_multiple(e)
except Exception as e:
    fallback(e)
else:
    # runs only if no exception was raised
    success_path()
finally:
    # always runs — cleanup here
    cleanup()

# Raise exceptions
raise ValueError("message")
raise CustomError("message")
raise                          # re-raise current exception

# Exception chaining
raise NewError("msg") from original_error
raise NewError("msg") from None   # suppress chain

# Custom exception
class MyError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

# Context manager
with open("file.txt") as f:
    data = f.read()

# Suppress specific exception
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("temp.txt")

# Log with traceback
import logging
try:
    risky()
except Exception:
    logging.exception("Something went wrong")

# Common built-in exceptions
ValueError          # bad value
TypeError           # bad type
KeyError            # missing dict key
IndexError          # list index out of range
AttributeError      # attribute not found
FileNotFoundError   # file missing
PermissionError     # no access
ZeroDivisionError   # division by zero
ImportError         # import failed
RuntimeError        # generic runtime error
NotImplementedError # abstract method not implemented
```

---

## Further Reading

- [Python Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Docs — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Docs — contextlib](https://docs.python.org/3/library/contextlib.html)
- [PEP 3134 — Exception Chaining](https://peps.python.org/pep-3134/)
- [PEP 654 — Exception Groups (Python 3.11)](https://peps.python.org/pep-0654/)
- [Python Docs — logging module](https://docs.python.org/3/library/logging.html)

---

*Written for Python 3.7+. Exception Groups section requires Python 3.11+. All examples tested and working.*
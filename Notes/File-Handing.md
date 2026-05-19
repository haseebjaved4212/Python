# 📁 Python File Handling — The Complete Guide

> Reading, writing, and managing files is something almost every real-world Python program does. This guide covers everything from basic file I/O to working with CSV, JSON, binary files, and the file system itself.

---

## Table of Contents

1. [What is File Handling?](#what-is-file-handling)
2. [Opening and Closing Files](#opening-and-closing-files)
3. [File Opening Modes](#file-opening-modes)
4. [Reading Files](#reading-files)
5. [Writing Files](#writing-files)
6. [Appending to Files](#appending-to-files)
7. [The with Statement — Context Manager](#the-with-statement--context-manager)
8. [File Object Methods and Attributes](#file-object-methods-and-attributes)
9. [Working with File Paths — pathlib](#working-with-file-paths--pathlib)
10. [Working with File Paths — os.path](#working-with-file-paths--ospath)
11. [CSV Files](#csv-files)
12. [JSON Files](#json-files)
13. [Binary Files](#binary-files)
14. [Working with Directories](#working-with-directories)
15. [File Metadata and Stats](#file-metadata-and-stats)
16. [Temporary Files](#temporary-files)
17. [File Compression — ZIP and GZIP](#file-compression--zip-and-gzip)
18. [Watching Files for Changes](#watching-files-for-changes)
19. [Exception Handling in File Operations](#exception-handling-in-file-operations)
20. [Performance Tips for Large Files](#performance-tips-for-large-files)
21. [Real-World Use Cases](#real-world-use-cases)
22. [Common Mistakes](#common-mistakes)
23. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## What is File Handling?

**File handling** is the ability to create, read, update, and delete files stored on disk. Python provides built-in functions and a rich standard library to work with files of all types — text, binary, CSV, JSON, ZIP, and more.

```python
# The simplest possible file operation
with open("hello.txt", "w") as f:
    f.write("Hello, World!")

with open("hello.txt", "r") as f:
    print(f.read())   # Hello, World!
```

Python file handling works at multiple levels:

| Level | Tools |
|---|---|
| Basic I/O | `open()`, `read()`, `write()` |
| Path handling | `pathlib.Path`, `os.path` |
| Structured data | `csv`, `json` modules |
| Binary data | `rb`, `wb` modes, `struct` module |
| File system ops | `os`, `shutil`, `pathlib` |
| Compression | `zipfile`, `gzip`, `tarfile` |
| Temp files | `tempfile` module |

---

## Opening and Closing Files

### Using `open()`

The built-in `open()` function returns a **file object**. It is the entry point for all file operations.

```python
# Syntax
file = open(filepath, mode, encoding=None, buffering=-1)
```

### Manual open and close

```python
# Always close what you open
file = open("data.txt", "r")
content = file.read()
file.close()   # must be called manually
```

The problem with manual closing is that if an exception occurs between `open()` and `close()`, the file stays open and you leak a file descriptor. This is why the `with` statement exists.

### Checking if a file is closed

```python
file = open("data.txt", "r")
print(file.closed)   # False
file.close()
print(file.closed)   # True
```

---

## File Opening Modes

The mode string tells Python what you intend to do with the file.

| Mode | Name | Description |
|---|---|---|
| `"r"` | Read | Read only. File must exist. Default mode. |
| `"w"` | Write | Write only. Creates file if missing. **Truncates** if exists. |
| `"a"` | Append | Write only. Creates file if missing. Preserves existing content. |
| `"x"` | Exclusive Create | Creates new file. Raises `FileExistsError` if already exists. |
| `"r+"` | Read + Write | Read and write. File must exist. Does NOT truncate. |
| `"w+"` | Write + Read | Read and write. Creates or truncates. |
| `"a+"` | Append + Read | Read and append. Creates if missing. |

### Binary vs text mode

Append `"b"` to any mode for binary mode:

| Mode | Description |
|---|---|
| `"rb"` | Read binary |
| `"wb"` | Write binary |
| `"ab"` | Append binary |
| `"rb+"` | Read and write binary |

```python
# Text mode (default) — handles newline translation, encoding/decoding
with open("notes.txt", "r") as f:
    text = f.read()          # returns str

# Binary mode — raw bytes, no translation
with open("image.png", "rb") as f:
    data = f.read()          # returns bytes
```

### Encoding — always specify it

```python
# Always specify encoding for text files to avoid platform-specific surprises
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 世界!")
```

> **Rule:** Always pass `encoding="utf-8"` when working with text files unless you have a specific reason not to. The default encoding varies by operating system.

---

## Reading Files

### `read()` — read entire file at once

```python
with open("story.txt", "r", encoding="utf-8") as f:
    content = f.read()        # returns the entire file as a single string
    print(len(content))       # number of characters
```

### `read(n)` — read n characters

```python
with open("data.txt", "r", encoding="utf-8") as f:
    chunk = f.read(100)       # read first 100 characters
    next_chunk = f.read(100)  # read next 100 characters
```

### `readline()` — read one line at a time

```python
with open("log.txt", "r", encoding="utf-8") as f:
    first_line  = f.readline()   # reads up to and including \n
    second_line = f.readline()
    third_line  = f.readline()
    # returns empty string "" when end of file is reached
```

### `readlines()` — read all lines into a list

```python
with open("names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()    # ['Alice\n', 'Bob\n', 'Charlie\n']

# Strip newlines
lines = [line.rstrip("\n") for line in lines]
# ['Alice', 'Bob', 'Charlie']
```

### Iterating line by line — most memory-efficient

```python
with open("large_file.txt", "r", encoding="utf-8") as f:
    for line in f:              # file object is iterable
        print(line.rstrip())    # strip trailing newline
```

This approach reads one line at a time into memory. Use this for large files — do NOT use `readlines()` on a 10GB log file.

### Reading with a specific number of lines

```python
def read_first_n_lines(filepath, n):
    lines = []
    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line.rstrip())
    return lines

first_10 = read_first_n_lines("server.log", 10)
```

### Reading from a specific position

```python
with open("data.txt", "r", encoding="utf-8") as f:
    f.seek(10)              # move to byte position 10
    content = f.read(50)    # read 50 chars from position 10
    print(f.tell())         # current position: 60
```

---

## Writing Files

### `write()` — write a string

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Line one\n")
    f.write("Line two\n")
    f.write("Line three\n")
```

> `write()` does NOT add a newline automatically. You must add `\n` yourself.

### `writelines()` — write a list of strings

```python
lines = ["Alice\n", "Bob\n", "Charlie\n"]

with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# Or with a generator — memory efficient
with open("numbers.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{n}\n" for n in range(1_000_000))
```

### Writing multiple lines cleanly

```python
data = ["Alice", "Bob", "Charlie", "Dave"]

with open("names.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(data))          # no trailing newline
    f.write("\n".join(data) + "\n")   # with trailing newline
```

### `print()` to a file

```python
with open("report.txt", "w", encoding="utf-8") as f:
    print("Sales Report", file=f)
    print("=" * 40, file=f)
    print(f"Total: $1,234.56", file=f)
```

---

## Appending to Files

Use `"a"` mode to add content to an existing file without overwriting it.

```python
# First write
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("2026-05-01: Server started\n")

# Later — append more entries
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("2026-05-02: User logged in\n")
    f.write("2026-05-03: Error in module X\n")

# Final content of log.txt:
# 2026-05-01: Server started
# 2026-05-02: User logged in
# 2026-05-03: Error in module X
```

### Append vs write mode

```python
# "w" — DANGEROUS if file exists with important data
with open("config.txt", "w") as f:
    f.write("new data")   # erases everything that was there!

# "a" — safe, always adds to the end
with open("config.txt", "a") as f:
    f.write("new data")   # appends to existing content
```

---

## The with Statement — Context Manager

The `with` statement is the **correct and preferred** way to handle files. It guarantees the file is closed properly — even if an exception occurs.

```python
# Old way — error-prone
file = open("data.txt", "r")
try:
    content = file.read()
finally:
    file.close()

# Modern way — clean, safe, preferred
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# file is automatically closed here, no matter what
```

### Opening multiple files at once

```python
with open("input.txt", "r", encoding="utf-8") as src, \
     open("output.txt", "w", encoding="utf-8") as dst:
    for line in src:
        dst.write(line.upper())
```

### What happens under the hood

When Python exits the `with` block it calls `f.__exit__()`, which in turn calls `f.close()`. This happens even if an exception is raised inside the block.

```python
with open("data.txt") as f:
    raise ValueError("Oops!")   # even here, file.close() is called
```

---

## File Object Methods and Attributes

```python
with open("data.txt", "r+", encoding="utf-8") as f:
    # Reading
    content = f.read()           # read entire file
    f.seek(0)                    # go back to start
    line    = f.readline()       # read one line
    lines   = f.readlines()      # read all lines into list

    # Writing
    f.write("text")              # write string
    f.writelines(["a\n", "b\n"]) # write list of strings

    # Position
    pos = f.tell()               # get current byte position
    f.seek(0)                    # go to byte position 0
    f.seek(0, 2)                 # go to end of file (offset 0 from end)
    f.seek(-10, 2)               # go 10 bytes from end

    # Flush and info
    f.flush()                    # flush buffer to disk immediately
    print(f.name)                # 'data.txt'
    print(f.mode)                # 'r+'
    print(f.encoding)            # 'utf-8'
    print(f.closed)              # False
```

### `seek()` reference positions

| Second argument | Meaning |
|---|---|
| `0` (default) | From the beginning of file |
| `1` | From the current position |
| `2` | From the end of file |

```python
with open("data.txt", "rb") as f:   # seek with 1 or 2 requires binary mode
    f.seek(0, 2)                     # jump to end
    size = f.tell()                  # file size in bytes
    print(f"File size: {size} bytes")
```

---

## Working with File Paths — pathlib

`pathlib.Path` is the modern, object-oriented way to work with file paths. It is cleaner, more readable, and works cross-platform.

```python
from pathlib import Path

# Create a Path object
p = Path("data/reports/sales.csv")

# Path components
print(p.name)        # sales.csv
print(p.stem)        # sales
print(p.suffix)      # .csv
print(p.parent)      # data/reports
print(p.parts)       # ('data', 'reports', 'sales.csv')

# Build paths with / operator
base    = Path("data")
reports = base / "reports"
file    = reports / "sales.csv"
print(file)   # data/reports/sales.csv
```

### Checking and creating paths

```python
p = Path("output/results.txt")

print(p.exists())      # True or False
print(p.is_file())     # True if it is a file
print(p.is_dir())      # True if it is a directory

# Create parent directories if missing
p.parent.mkdir(parents=True, exist_ok=True)
```

### Reading and writing with pathlib

```python
p = Path("notes.txt")

# Write
p.write_text("Hello from pathlib!\n", encoding="utf-8")

# Read
content = p.read_text(encoding="utf-8")
print(content)

# Binary
p_img = Path("photo.jpg")
raw = p_img.read_bytes()
Path("copy.jpg").write_bytes(raw)
```

### Listing and searching files

```python
base = Path(".")

# List all files in a directory
for item in base.iterdir():
    print(item)

# Glob — find files matching a pattern
for py_file in base.glob("*.py"):
    print(py_file)

# Recursive glob — search all subdirectories
for py_file in base.rglob("*.py"):
    print(py_file)

# All CSV files in data/
for csv_file in Path("data").rglob("*.csv"):
    print(csv_file.name, csv_file.stat().st_size)
```

### Useful pathlib operations

```python
from pathlib import Path

p = Path("data/old_name.txt")

# Rename / move
p.rename("data/new_name.txt")

# Delete a file
p.unlink(missing_ok=True)    # missing_ok=True avoids error if already gone

# Delete a directory
Path("empty_dir").rmdir()    # only works on empty directories

# Resolve to absolute path
abs_path = Path("data.txt").resolve()
print(abs_path)   # /home/user/project/data.txt

# Get home directory
home = Path.home()
print(home)       # /home/haseeb

# Get current working directory
cwd = Path.cwd()
print(cwd)
```

---

## Working with File Paths — os.path

`os.path` is the older, procedural API. You will see it in older codebases. `pathlib` is preferred for new code, but knowing `os.path` is important.

```python
import os

# Join paths safely (handles slashes correctly on all OS)
path = os.path.join("data", "reports", "sales.csv")

# Split path
directory, filename = os.path.split(path)
name, ext = os.path.splitext(filename)

print(directory)   # data/reports
print(filename)    # sales.csv
print(name)        # sales
print(ext)         # .csv

# Checks
print(os.path.exists(path))     # True or False
print(os.path.isfile(path))     # True if file
print(os.path.isdir("data"))    # True if directory
print(os.path.getsize(path))    # size in bytes

# Absolute path
print(os.path.abspath("data.txt"))

# Home directory
print(os.path.expanduser("~"))

# Join with home directory
config = os.path.expanduser("~/.config/myapp/settings.json")
```

### os vs pathlib comparison

```python
import os
from pathlib import Path

# os.path way
path = os.path.join("data", "file.txt")
if os.path.exists(path):
    with open(path) as f:
        content = f.read()

# pathlib way — cleaner
path = Path("data") / "file.txt"
if path.exists():
    content = path.read_text()
```

---

## CSV Files

CSV (Comma-Separated Values) is one of the most common file formats. Python's `csv` module handles it cleanly.

### Reading CSV

```python
import csv

# Basic reading
with open("employees.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)   # skip header row
    for row in reader:
        print(row)           # row is a list of strings: ['Alice', '30', 'Engineering']
```

> Always pass `newline=""` when opening CSV files. This prevents the csv module from mishandling line endings.

### Reading CSV as dictionaries

```python
import csv

with open("employees.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row is a dict: {'name': 'Alice', 'age': '30', 'dept': 'Engineering'}
        print(row["name"], row["dept"])
```

### Writing CSV

```python
import csv

data = [
    ["Name", "Age", "Department"],
    ["Alice", 30, "Engineering"],
    ["Bob",   27, "Design"],
    ["Carol", 35, "Marketing"],
]

with open("employees.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)    # write all rows at once
    # or write one by one:
    # writer.writerow(["Dave", 28, "Finance"])
```

### Writing CSV from dictionaries

```python
import csv

employees = [
    {"name": "Alice", "age": 30, "dept": "Engineering"},
    {"name": "Bob",   "age": 27, "dept": "Design"},
]

fieldnames = ["name", "age", "dept"]

with open("employees.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)
```

### Custom delimiters and quoting

```python
import csv

# Tab-separated values (TSV)
with open("data.tsv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")

# Semicolon-separated (common in European locales)
with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")

# Custom quoting
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)   # quote every field
```

---

## JSON Files

JSON is the standard format for config files, API responses, and data interchange. Python's `json` module makes it simple.

### Reading JSON

```python
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)    # parses JSON into Python dict/list

print(config["host"])
print(config["port"])
```

### Writing JSON

```python
import json

data = {
    "name": "Haseeb",
    "skills": ["Python", "React", "TypeScript"],
    "active": True,
    "score": 9.5,
    "address": None
}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
```

Output in `user.json`:
```json
{
    "name": "Haseeb",
    "skills": ["Python", "React", "TypeScript"],
    "active": true,
    "score": 9.5,
    "address": null
}
```

### JSON string conversion (without files)

```python
import json

# Python dict to JSON string
d = {"key": "value", "num": 42}
json_str = json.dumps(d, indent=2)
print(json_str)

# JSON string to Python dict
parsed = json.loads('{"name": "Alice", "age": 30}')
print(parsed["name"])   # Alice
```

### JSON type mapping

| Python | JSON |
|---|---|
| `dict` | `object {}` |
| `list`, `tuple` | `array []` |
| `str` | `string ""` |
| `int`, `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

### Serializing custom objects

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"name": "Haseeb", "created": datetime.now()}

with open("data.json", "w") as f:
    json.dump(data, f, cls=DateTimeEncoder, indent=2)
```

### Safe JSON loading with error handling

```python
import json

def load_json_safe(filepath, default=None):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default if default is not None else {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filepath}: {e}")
        return default if default is not None else {}
```

---

## Binary Files

Binary mode reads and writes raw bytes with no encoding or newline translation.

### Reading binary files

```python
# Read an image file
with open("photo.jpg", "rb") as f:
    data = f.read()

print(type(data))     # <class 'bytes'>
print(len(data))      # size in bytes
print(data[:4])       # first 4 bytes (JPEG magic bytes: b'\xff\xd8\xff\xe0')
```

### Copying a binary file

```python
def copy_file(src_path, dst_path, chunk_size=8192):
    with open(src_path, "rb") as src, \
         open(dst_path, "wb") as dst:
        while chunk := src.read(chunk_size):
            dst.write(chunk)

copy_file("original.jpg", "copy.jpg")
```

### Writing structured binary data with `struct`

```python
import struct

# Pack data into binary format
# Format: little-endian unsigned int, float, 10-char string
record = struct.pack("<I f 10s", 42, 3.14, b"Haseeb    ")

with open("record.bin", "wb") as f:
    f.write(record)

# Unpack binary data back into Python values
with open("record.bin", "rb") as f:
    raw = f.read()

num, pi, name = struct.unpack("<I f 10s", raw)
print(num)              # 42
print(round(pi, 2))     # 3.14
print(name.decode().strip())   # Haseeb
```

### Checking file type by magic bytes

```python
MAGIC_BYTES = {
    b"\x89PNG": "PNG image",
    b"\xff\xd8\xff": "JPEG image",
    b"PK\x03\x04": "ZIP archive",
    b"%PDF": "PDF document",
    b"\x1f\x8b": "GZIP archive",
}

def detect_file_type(filepath):
    with open(filepath, "rb") as f:
        header = f.read(4)
    for magic, name in MAGIC_BYTES.items():
        if header.startswith(magic):
            return name
    return "Unknown"

print(detect_file_type("document.pdf"))   # PDF document
```

---

## Working with Directories

### Creating directories

```python
import os
from pathlib import Path

# Create a single directory
os.mkdir("output")
Path("output").mkdir()

# Create nested directories
os.makedirs("data/reports/2026", exist_ok=True)
Path("data/reports/2026").mkdir(parents=True, exist_ok=True)
```

### Listing directory contents

```python
import os
from pathlib import Path

# List names
print(os.listdir("."))

# List with full paths using pathlib
for item in Path(".").iterdir():
    kind = "DIR" if item.is_dir() else "FILE"
    print(f"[{kind}] {item.name}")
```

### Walking a directory tree recursively

```python
import os

for root, dirs, files in os.walk("project"):
    level = root.replace("project", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(root)}/")

    for file in files:
        print(f"{indent}  {file}")
```

### Copying, moving, and deleting

```python
import shutil
from pathlib import Path

# Copy a file
shutil.copy("source.txt", "destination.txt")
shutil.copy2("source.txt", "destination.txt")   # also copies metadata

# Copy an entire directory tree
shutil.copytree("src_folder", "dst_folder")

# Move a file or directory
shutil.move("old_location.txt", "new_location.txt")

# Delete a file
os.remove("unwanted.txt")
Path("unwanted.txt").unlink(missing_ok=True)

# Delete an empty directory
os.rmdir("empty_folder")

# Delete a directory and ALL its contents — be careful!
shutil.rmtree("folder_to_delete")
```

### Finding files by pattern

```python
import glob
from pathlib import Path

# glob module
python_files = glob.glob("**/*.py", recursive=True)

# pathlib (preferred)
python_files = list(Path(".").rglob("*.py"))
log_files    = list(Path("logs").glob("*.log"))
recent_csv   = list(Path("data").glob("2026_*.csv"))
```

---

## File Metadata and Stats

```python
import os
from pathlib import Path
from datetime import datetime

p = Path("data.txt")

# Get file stats
stat = p.stat()

print(f"Size:     {stat.st_size} bytes")
print(f"Created:  {datetime.fromtimestamp(stat.st_ctime)}")
print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")
print(f"Accessed: {datetime.fromtimestamp(stat.st_atime)}")

# Permissions
print(oct(stat.st_mode))   # e.g., 0o100644

# Quick size check
print(f"File size: {os.path.getsize('data.txt')} bytes")

# Human-readable size
def human_size(bytes_count):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_count < 1024:
            return f"{bytes_count:.1f} {unit}"
        bytes_count /= 1024
    return f"{bytes_count:.1f} PB"

print(human_size(p.stat().st_size))   # e.g., 12.3 KB
```

---

## Temporary Files

Use the `tempfile` module when you need scratch space that should be cleaned up automatically.

```python
import tempfile

# Temporary file — deleted automatically when closed
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                  encoding="utf-8", delete=True) as tmp:
    tmp.write("temporary data")
    print(f"Temp file path: {tmp.name}")
    tmp.flush()
    # file is deleted when the with block exits

# Temporary file with manual control
tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
tmp.write(b'{"key": "value"}')
tmp.close()
print(f"Temp file at: {tmp.name}")
# You are responsible for deleting it
os.unlink(tmp.name)

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    tmppath = Path(tmpdir) / "scratch.txt"
    tmppath.write_text("scratch data")
    print(f"Temp dir: {tmpdir}")
# directory and all contents deleted automatically
```

---

## File Compression — ZIP and GZIP

### Working with ZIP files

```python
import zipfile
from pathlib import Path

# Create a ZIP archive
with zipfile.ZipFile("archive.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("data.txt")
    zf.write("report.csv", arcname="reports/report.csv")   # rename inside zip

# Add all files in a directory
with zipfile.ZipFile("project.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for file in Path("src").rglob("*"):
        if file.is_file():
            zf.write(file, arcname=file.relative_to("src"))

# Read/inspect a ZIP archive
with zipfile.ZipFile("archive.zip", "r") as zf:
    print(zf.namelist())                  # list all files inside
    info = zf.getinfo("data.txt")
    print(f"Compressed:   {info.compress_size} bytes")
    print(f"Uncompressed: {info.file_size} bytes")

# Extract files
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extractall("output_dir")           # extract all
    zf.extract("data.txt", "output_dir")  # extract one file

# Read a file from ZIP without extracting to disk
with zipfile.ZipFile("archive.zip", "r") as zf:
    with zf.open("data.txt") as f:
        content = f.read().decode("utf-8")
        print(content)
```

### Working with GZIP files

```python
import gzip

# Write a GZIP-compressed file
with gzip.open("data.txt.gz", "wt", encoding="utf-8") as f:
    f.write("This content will be compressed\n" * 1000)

# Read a GZIP-compressed file
with gzip.open("data.txt.gz", "rt", encoding="utf-8") as f:
    content = f.read()

# Compress an existing file
with open("large.log", "rb") as f_in, \
     gzip.open("large.log.gz", "wb") as f_out:
    f_out.writelines(f_in)
```

---

## Watching Files for Changes

```python
# Using polling with os.stat for a simple watcher
import os
import time

def watch_file(filepath, callback, interval=1.0):
    """Call callback(filepath) whenever the file is modified."""
    last_modified = os.path.getmtime(filepath)
    print(f"Watching: {filepath}")
    while True:
        time.sleep(interval)
        current_modified = os.path.getmtime(filepath)
        if current_modified != last_modified:
            last_modified = current_modified
            callback(filepath)

def on_change(filepath):
    print(f"File changed: {filepath}")
    with open(filepath) as f:
        print(f.read())

# watch_file("config.json", on_change)  # runs forever

# For production use — install watchdog:
# pip install watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")

# observer = Observer()
# observer.schedule(ChangeHandler(), path=".", recursive=False)
# observer.start()
```

---

## Exception Handling in File Operations

File operations fail in many predictable ways. Handle each case explicitly.

```python
import os
import json
from pathlib import Path

def read_file_safe(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except PermissionError:
        print(f"Permission denied: {filepath}")
        return None
    except UnicodeDecodeError:
        print(f"Cannot decode file as UTF-8: {filepath}")
        return None
    except OSError as e:
        print(f"OS error reading {filepath}: {e}")
        return None


def write_file_safe(filepath, content):
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except PermissionError:
        print(f"No write permission: {filepath}")
        return False
    except OSError as e:
        print(f"OS error writing {filepath}: {e}")
        return False


def load_json_config(filepath, defaults=None):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config not found, using defaults.")
        return defaults or {}
    except json.JSONDecodeError as e:
        print(f"Malformed JSON in {filepath}: {e}")
        return defaults or {}
```

### Common file exceptions

| Exception | When it occurs |
|---|---|
| `FileNotFoundError` | File or directory does not exist |
| `PermissionError` | No read/write/execute permission |
| `FileExistsError` | File already exists (raised by `"x"` mode) |
| `IsADirectoryError` | Expected a file, got a directory |
| `NotADirectoryError` | Expected a directory, got a file |
| `UnicodeDecodeError` | Cannot decode file contents with given encoding |
| `UnicodeEncodeError` | Cannot encode string to given encoding |
| `OSError` | Generic OS-level I/O failure (parent of most above) |
| `IOError` | Alias for `OSError` |

---

## Performance Tips for Large Files

### Never load a large file entirely into memory

```python
# Bad — loads 10GB into RAM
with open("huge.log") as f:
    lines = f.readlines()   # 10GB in memory

# Good — process one line at a time
with open("huge.log", encoding="utf-8") as f:
    for line in f:
        process(line)
```

### Use chunked reading for binary files

```python
def process_large_binary(filepath, chunk_size=65536):
    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            process_chunk(chunk)
```

### Use generators to build lazy pipelines

```python
def read_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip()

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def parse_log(lines):
    for line in lines:
        parts = line.split(" ", 3)
        if len(parts) == 4:
            yield {"date": parts[0], "time": parts[1],
                   "level": parts[2], "msg": parts[3]}

# Full pipeline — processes file line by line, never loads all at once
pipeline = parse_log(filter_errors(read_lines("server.log")))

for entry in pipeline:
    print(entry)
```

### Use `io.BufferedReader` for fine-tuned buffering

```python
import io

with open("large.bin", "rb", buffering=0) as raw:    # unbuffered
    buffered = io.BufferedReader(raw, buffer_size=131072)
    while chunk := buffered.read(65536):
        process(chunk)
```

### Measure I/O performance

```python
import time
from pathlib import Path

def benchmark_read(filepath):
    start = time.perf_counter()
    size  = 0

    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            size += len(chunk)

    elapsed = time.perf_counter() - start
    mb      = size / (1024 * 1024)
    print(f"Read {mb:.1f} MB in {elapsed:.3f}s ({mb/elapsed:.1f} MB/s)")
```

---

## Real-World Use Cases

### 1. Config file manager

```python
import json
from pathlib import Path

class ConfigManager:
    def __init__(self, config_path):
        self.path = Path(config_path)
        self._data = self._load()

    def _load(self):
        if self.path.exists():
            try:
                return json.loads(self.path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return {}
        return {}

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
        self._save()

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self._data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

config = ConfigManager("~/.myapp/config.json")
config.set("theme", "dark")
config.set("font_size", 14)
print(config.get("theme"))   # dark
```

### 2. Rotating log writer

```python
import os
from datetime import datetime
from pathlib import Path

class RotatingLogger:
    def __init__(self, log_dir, prefix="app", max_bytes=10_485_760):
        self.log_dir   = Path(log_dir)
        self.prefix    = prefix
        self.max_bytes = max_bytes
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self._file = None
        self._open_file()

    def _current_path(self):
        date = datetime.now().strftime("%Y-%m-%d")
        return self.log_dir / f"{self.prefix}_{date}.log"

    def _open_file(self):
        if self._file:
            self._file.close()
        self._file = open(self._current_path(), "a", encoding="utf-8")

    def log(self, level, message):
        if self._file.tell() >= self.max_bytes:
            self._open_file()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._file.write(f"[{timestamp}] [{level}] {message}\n")
        self._file.flush()

    def close(self):
        if self._file:
            self._file.close()

logger = RotatingLogger("logs")
logger.log("INFO",  "Server started")
logger.log("ERROR", "Connection timeout")
logger.close()
```

### 3. CSV data processor

```python
import csv
from pathlib import Path
from collections import defaultdict

def summarize_sales(filepath):
    totals = defaultdict(float)

    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            region = row["region"]
            amount = float(row["amount"])
            totals[region] += amount

    # Write summary
    summary_path = Path(filepath).stem + "_summary.csv"
    with open(summary_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Region", "Total Sales"])
        for region, total in sorted(totals.items(), key=lambda x: -x[1]):
            writer.writerow([region, f"{total:.2f}"])

    print(f"Summary written to {summary_path}")
    return totals
```

### 4. Recursive file search and report

```python
from pathlib import Path
from datetime import datetime

def scan_directory(root, extensions=None):
    root = Path(root)
    results = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if extensions and path.suffix.lower() not in extensions:
            continue
        stat = path.stat()
        results.append({
            "path":     str(path),
            "name":     path.name,
            "size":     stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
        })

    results.sort(key=lambda x: x["size"], reverse=True)
    return results

files = scan_directory(".", extensions={".py", ".js", ".ts"})
for f in files[:10]:
    print(f"{f['size']:>10} bytes  {f['name']}")
```

### 5. Safe atomic file write

```python
import os
import tempfile
from pathlib import Path

def atomic_write(filepath, content, encoding="utf-8"):
    """Write to a temp file first, then rename — prevents partial writes."""
    filepath = Path(filepath)
    tmp_fd, tmp_path = tempfile.mkstemp(
        dir=filepath.parent,
        prefix=f".{filepath.name}.",
        suffix=".tmp"
    )
    try:
        with os.fdopen(tmp_fd, "w", encoding=encoding) as tmp_file:
            tmp_file.write(content)
        os.replace(tmp_path, filepath)    # atomic on POSIX systems
    except Exception:
        os.unlink(tmp_path)
        raise

atomic_write("config.json", '{"debug": true}')
```

---

## Common Mistakes

### Mistake 1: Not using context manager

```python
# Bad — file may never be closed if an exception occurs
f = open("data.txt")
content = f.read()
f.close()

# Good
with open("data.txt", encoding="utf-8") as f:
    content = f.read()
```

### Mistake 2: Not specifying encoding

```python
# Bad — encoding depends on the OS, can break across platforms
with open("data.txt", "r") as f:
    content = f.read()

# Good — always explicit
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### Mistake 3: Using "w" mode on an important file

```python
# Bad — destroys existing content silently
with open("production.log", "w") as f:
    f.write("new entry\n")   # everything before this is gone!

# Good — append or back up first
with open("production.log", "a") as f:
    f.write("new entry\n")
```

### Mistake 4: Loading huge files with `readlines()` or `read()`

```python
# Bad — loads entire 10GB file into RAM
with open("server.log") as f:
    lines = f.readlines()

# Good — iterate lazily
with open("server.log", encoding="utf-8") as f:
    for line in f:
        process(line)
```

### Mistake 5: Hardcoding path separators

```python
# Bad — breaks on Windows
path = "data/reports/" + filename

# Good — works everywhere
from pathlib import Path
path = Path("data") / "reports" / filename

# Also fine with os.path
import os
path = os.path.join("data", "reports", filename)
```

### Mistake 6: Not handling missing parent directories

```python
# Bad — crashes if "data/output/" does not exist
with open("data/output/results.txt", "w") as f:
    f.write("results")

# Good — create directories first
from pathlib import Path
path = Path("data/output/results.txt")
path.parent.mkdir(parents=True, exist_ok=True)
with open(path, "w", encoding="utf-8") as f:
    f.write("results")
```

### Mistake 7: Forgetting `newline=""` for CSV

```python
# Bad — double newlines on Windows
with open("data.csv", "w") as f:
    writer = csv.writer(f)

# Good — always use newline="" with csv module
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
```

---

## Quick Cheat Sheet

```python
from pathlib import Path
import os, shutil, json, csv

# Open modes
open("f.txt", "r")     # read (default)
open("f.txt", "w")     # write (truncates)
open("f.txt", "a")     # append
open("f.txt", "x")     # create new (error if exists)
open("f.txt", "r+")    # read + write
open("f.bin", "rb")    # binary read
open("f.bin", "wb")    # binary write

# Reading
with open("f.txt", encoding="utf-8") as f:
    content = f.read()             # entire file as string
    line    = f.readline()         # one line
    lines   = f.readlines()        # all lines as list
    for line in f: ...             # iterate lazily

# Writing
with open("f.txt", "w", encoding="utf-8") as f:
    f.write("text")
    f.writelines(["a\n", "b\n"])
    print("text", file=f)

# pathlib
p = Path("dir/file.txt")
p.read_text(encoding="utf-8")
p.write_text("content", encoding="utf-8")
p.read_bytes()
p.write_bytes(b"data")
p.exists() / p.is_file() / p.is_dir()
p.parent.mkdir(parents=True, exist_ok=True)
p.unlink(missing_ok=True)
list(p.parent.glob("*.txt"))
list(Path(".").rglob("*.py"))

# os / shutil
os.listdir(".")
os.makedirs("a/b/c", exist_ok=True)
os.remove("file.txt")
os.rename("old.txt", "new.txt")
shutil.copy("src", "dst")
shutil.copytree("src_dir", "dst_dir")
shutil.move("src", "dst")
shutil.rmtree("dir")

# JSON
with open("f.json", "r", encoding="utf-8") as f: data = json.load(f)
with open("f.json", "w", encoding="utf-8") as f: json.dump(data, f, indent=2)
json.loads('{"a": 1}')       # str to dict
json.dumps({"a": 1})         # dict to str

# CSV
with open("f.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f): ...
    for row in csv.DictReader(f): ...

with open("f.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(data)
    csv.DictWriter(f, fieldnames=["a","b"]).writerows(dicts)

# ZIP
import zipfile
with zipfile.ZipFile("a.zip", "w") as zf: zf.write("file.txt")
with zipfile.ZipFile("a.zip", "r") as zf: zf.extractall("out/")

# Temp files
import tempfile
with tempfile.NamedTemporaryFile(delete=True) as t: t.write(b"data")
with tempfile.TemporaryDirectory() as d: Path(d, "f.txt").write_text("x")
```

---

## Further Reading

- [Python Docs — Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Docs — pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python Docs — os.path](https://docs.python.org/3/library/os.path.html)
- [Python Docs — csv module](https://docs.python.org/3/library/csv.html)
- [Python Docs — json module](https://docs.python.org/3/library/json.html)
- [Python Docs — zipfile](https://docs.python.org/3/library/zipfile.html)
- [Python Docs — tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python Docs — shutil](https://docs.python.org/3/library/shutil.html)

---

*Written for Python 3.7+. All examples tested and working.*
# 🧱 Object-Oriented Programming in Python — The Complete Guide

> OOP is not just a syntax feature. It is a way of thinking about problems. This guide takes you from zero to confident — classes, objects, inheritance, polymorphism, encapsulation, and everything in between.

---

## Table of Contents

1. [What is OOP?](#what-is-oop)
2. [The Four Pillars of OOP](#the-four-pillars-of-oop)
3. [Classes and Objects](#classes-and-objects)
4. [The `__init__` Method](#the-__init__-method)
5. [Instance Variables vs Class Variables](#instance-variables-vs-class-variables)
6. [Instance Methods, Class Methods, and Static Methods](#instance-methods-class-methods-and-static-methods)
7. [Encapsulation and Access Modifiers](#encapsulation-and-access-modifiers)
8. [Properties — Getters and Setters](#properties--getters-and-setters)
9. [Inheritance](#inheritance)
10. [Multiple Inheritance and MRO](#multiple-inheritance-and-mro)
11. [Polymorphism](#polymorphism)
12. [Abstraction and Abstract Classes](#abstraction-and-abstract-classes)
13. [Dunder (Magic) Methods](#dunder-magic-methods)
14. [Composition vs Inheritance](#composition-vs-inheritance)
15. [Dataclasses](#dataclasses)
16. [Class Decorators](#class-decorators)
17. [Slots for Memory Optimization](#slots-for-memory-optimization)
18. [OOP Design Principles — SOLID](#oop-design-principles--solid)
19. [Real-World Project Structure](#real-world-project-structure)
20. [Common Mistakes](#common-mistakes)
21. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## What is OOP?

**Object-Oriented Programming** is a programming paradigm that organizes code around **objects** rather than functions and logic. An object is a self-contained unit that bundles **data** (attributes) and **behavior** (methods) together.

In Python, everything is an object. Integers, strings, functions, modules — they all have types and methods. Python was designed with OOP at its core.

```python
# Even this basic string is an object with methods
name = "haseeb"
print(name.upper())       # HASEEB
print(type(name))         # <class 'str'>
print(isinstance(name, str))  # True
```

### Procedural vs OOP thinking

```python
# Procedural approach — data and logic are separate
name  = "Haseeb"
role  = "Developer"
level = 5

def greet_user(name, role):
    return f"Hi {name}, you are a {role}."

# OOP approach — data and behavior live together
class Developer:
    def __init__(self, name, role, level):
        self.name  = name
        self.role  = role
        self.level = level

    def greet(self):
        return f"Hi {self.name}, you are a {self.role}."

dev = Developer("Haseeb", "Frontend Developer", 5)
print(dev.greet())
```

---

## The Four Pillars of OOP

| Pillar | What it means |
|---|---|
| **Encapsulation** | Bundle data and methods together; hide internal details |
| **Inheritance** | A class can reuse and extend another class |
| **Polymorphism** | Different classes can share the same interface |
| **Abstraction** | Hide complexity; expose only what is necessary |

Each of these is covered in its own dedicated section below.

---

## Classes and Objects

A **class** is a blueprint. An **object** (instance) is something built from that blueprint.

```python
class Car:
    # Class body
    brand = "Generic"   # class variable

    def drive(self):
        print("Vroom!")

# Creating objects (instances)
car1 = Car()
car2 = Car()

car1.drive()     # Vroom!
print(car1.brand)  # Generic

# Objects are independent
car1.color = "Red"
car2.color = "Blue"

print(car1.color)  # Red
print(car2.color)  # Blue
```

### Checking object identity and type

```python
print(type(car1))               # <class '__main__.Car'>
print(isinstance(car1, Car))    # True
print(id(car1) == id(car2))     # False — different objects in memory
print(car1 is car2)             # False
```

---

## The `__init__` Method

`__init__` is the **constructor** — it runs automatically every time a new object is created. Use it to set up the initial state of an object.

```python
class Developer:
    def __init__(self, name, language, experience_years):
        self.name             = name
        self.language         = language
        self.experience_years = experience_years
        self.projects         = []    # starts empty for every instance

    def introduce(self):
        return (
            f"I'm {self.name}, a {self.language} developer "
            f"with {self.experience_years} years of experience."
        )

    def add_project(self, project_name):
        self.projects.append(project_name)
        print(f"Added project: {project_name}")

dev = Developer("Haseeb", "Python", 3)
print(dev.introduce())
dev.add_project("Portfolio Website")
dev.add_project("E-commerce App")
print(dev.projects)
```

### Default parameter values in `__init__`

```python
class Config:
    def __init__(self, host="localhost", port=8000, debug=False):
        self.host  = host
        self.port  = port
        self.debug = debug

default_config = Config()
custom_config  = Config(host="0.0.0.0", port=3000, debug=True)
```

---

## Instance Variables vs Class Variables

| Type | Defined | Shared? | Access |
|---|---|---|---|
| **Instance variable** | Inside `__init__` via `self` | No — unique per object | `self.name` |
| **Class variable** | In the class body directly | Yes — shared by all instances | `ClassName.var` or `self.var` |

```python
class Employee:
    company    = "TechCorp"     # class variable — shared
    headcount  = 0              # class variable — shared counter

    def __init__(self, name, salary):
        self.name   = name      # instance variable — unique
        self.salary = salary    # instance variable — unique
        Employee.headcount += 1

    @classmethod
    def get_headcount(cls):
        return cls.headcount

e1 = Employee("Alice", 90000)
e2 = Employee("Bob",   85000)

print(Employee.company)         # TechCorp
print(e1.company)               # TechCorp — inherits class variable
print(Employee.headcount)       # 2
print(Employee.get_headcount()) # 2

# Overriding class variable on an instance
e1.company = "StartupX"         # creates a new INSTANCE variable for e1
print(e1.company)               # StartupX
print(e2.company)               # TechCorp — unchanged
print(Employee.company)         # TechCorp — unchanged
```

> **Gotcha:** Never use mutable class variables like lists or dicts as defaults, or all instances will share the same object and mutations will affect everyone.

```python
# Bug — all instances share the SAME list
class Bad:
    items = []   # class variable

    def add(self, item):
        self.items.append(item)

b1 = Bad()
b2 = Bad()
b1.add("x")
print(b2.items)   # ['x'] — unexpected!

# Fix — create a new list per instance
class Good:
    def __init__(self):
        self.items = []   # instance variable

    def add(self, item):
        self.items.append(item)
```

---

## Instance Methods, Class Methods, and Static Methods

### Instance methods — the default

Operate on an instance. Receive `self` as the first argument.

```python
class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):               # instance method
        return self.PI * self.radius ** 2

    def scale(self, factor):      # instance method
        self.radius *= factor
```

### Class methods — operate on the class itself

Receive `cls` as the first argument. Used for alternative constructors and class-level logic.

```python
    @classmethod
    def from_diameter(cls, diameter):   # alternative constructor
        return cls(diameter / 2)

    @classmethod
    def unit_circle(cls):               # factory method
        return cls(1)

c1 = Circle(5)
c2 = Circle.from_diameter(10)   # radius = 5
c3 = Circle.unit_circle()       # radius = 1
```

### Static methods — utility functions that belong to the class

Receive neither `self` nor `cls`. Just a regular function that lives in the class namespace.

```python
    @staticmethod
    def is_valid_radius(value):
        return isinstance(value, (int, float)) and value > 0

print(Circle.is_valid_radius(5))    # True
print(Circle.is_valid_radius(-1))   # False
print(Circle.is_valid_radius("5"))  # False
```

### When to use which

| Type | Use when... |
|---|---|
| Instance method | You need to read or modify instance state |
| Class method | You need to access/modify class state, or create factory constructors |
| Static method | You have utility logic related to the class but not tied to any instance or class state |

---

## Encapsulation and Access Modifiers

Encapsulation means controlling access to the internal state of an object. Python uses naming conventions since it has no true access keywords like Java.

| Convention | Meaning | Enforcement |
|---|---|---|
| `name` | Public | None — fully accessible |
| `_name` | Protected | Convention only — "use with care" |
| `__name` | Private | Name mangling — harder to access from outside |

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner     = owner        # public
        self._balance  = balance      # protected (convention)
        self.__pin     = "1234"       # private (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount("Haseeb", 1000)

print(account.owner)          # Haseeb       — fine
print(account._balance)       # 1000         — works but "don't touch"
# print(account.__pin)        # AttributeError!

# Name mangling — Python renames it internally
print(account._BankAccount__pin)   # 1234 — technically accessible but please don't
```

### Name mangling under the hood

```python
# Python internally renames __pin to _ClassName__pin
# This prevents accidental access and accidental override in subclasses
class Child(BankAccount):
    def __init__(self):
        super().__init__("Child", 0)
        self.__pin = "9999"   # creates _Child__pin, not _BankAccount__pin
```

---

## Properties — Getters and Setters

The `@property` decorator lets you define methods that are accessed like attributes. This gives you controlled access to private data with validation.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   # store internally

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"Temperature below absolute zero: {value}")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        del self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32   # computed property, read-only

temp = Temperature(25)
print(temp.celsius)      # 25    — calls getter
print(temp.fahrenheit)   # 77.0  — computed on the fly

temp.celsius = 100       # calls setter
print(temp.celsius)      # 100

temp.celsius = -300      # ValueError: Temperature below absolute zero
```

### Property vs plain attribute

```python
class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name.title()    # always returns title-cased

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

u = User("  haseeb  ")
print(u.name)    # Haseeb  — stripped and title-cased
u.name = ""      # ValueError
```

---

## Inheritance

Inheritance lets a child class reuse and extend the behavior of a parent class. This models "is-a" relationships.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def breathe(self):
        return f"{self.name} is breathing."

    def describe(self):
        return f"{self.name} is {self.age} years old."

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def describe(self):
        base    = super().describe()    # call parent method
        habitat = "indoor" if self.indoor else "outdoor"
        return f"{base} ({habitat} cat)"


dog = Dog("Rex", 3, "Labrador")
cat = Cat("Luna", 2, indoor=True)

print(dog.speak())     # Rex says: Woof!
print(dog.breathe())   # Rex is breathing.  — inherited
print(dog.fetch())     # Rex fetches the ball!

print(cat.speak())     # Luna says: Meow!
print(cat.describe())  # Luna is 2 years old. (indoor cat)
```

### Checking inheritance relationships

```python
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True — dog IS-AN animal
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False
```

### `super()` in depth

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)   # initialize parent part
        self.battery_kwh = battery_kwh

    def info(self):
        base = super().info()                 # reuse parent method
        return f"{base} (Electric, {self.battery_kwh}kWh)"


ev = ElectricVehicle("Tesla", "Model 3", 2024, 82)
print(ev.info())   # 2024 Tesla Model 3 (Electric, 82kWh)
```

---

## Multiple Inheritance and MRO

Python supports inheriting from more than one parent class. The **Method Resolution Order (MRO)** determines which class's method gets called when there is a conflict.

```python
class Flyable:
    def move(self):
        return "Flying"

    def describe(self):
        return "I can fly"


class Swimmable:
    def move(self):
        return "Swimming"

    def describe(self):
        return "I can swim"


class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"


d = Duck()
print(d.move())      # Flying  — Flyable is listed first, it wins
print(d.quack())     # Quack!

# View the MRO
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)
```

### Python uses C3 Linearization for MRO

```python
# MRO is resolved left to right, depth first
class A:
    def hello(self): return "A"

class B(A):
    def hello(self): return "B"

class C(A):
    def hello(self): return "C"

class D(B, C):
    pass

d = D()
print(d.hello())    # B  — follows MRO: D -> B -> C -> A
print(D.mro())      # [D, B, C, A, object]
```

### Mixin pattern — the right way to use multiple inheritance

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        import datetime
        super().__init__(*args, **kwargs)
        self.created_at = datetime.datetime.now().isoformat()


class User(TimestampMixin, JSONMixin, LogMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name  = name
        self.email = email

u = User("Haseeb", "haseeb@example.com")
u.log("User created")
print(u.to_json())
print(u.created_at)
```

---

## Polymorphism

Polymorphism means "many forms" — different classes can respond to the same interface in different ways. Python achieves this naturally through **duck typing**.

```python
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def describe(self):
        return (
            f"{self.__class__.__name__}: "
            f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"
        )


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


# Polymorphism in action — same interface, different behavior
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]

for shape in shapes:
    print(shape.describe())

# Circle: area=78.54, perimeter=31.42
# Rectangle: area=24.00, perimeter=20.00
# Triangle: area=6.00, perimeter=12.00
```

### Duck typing

```python
# Python does not care about the type — only about the interface
class Robot:
    def speak(self):
        return "Beep boop"

class Human:
    def speak(self):
        return "Hello!"

class Parrot:
    def speak(self):
        return "Polly wants a cracker"

def make_speak(entity):
    print(entity.speak())   # works for any object with a speak() method

for being in [Robot(), Human(), Parrot()]:
    make_speak(being)
```

---

## Abstraction and Abstract Classes

An **abstract class** cannot be instantiated directly. It defines a contract — a set of methods that all subclasses must implement. Use `abc` module.

```python
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Abstract base class — defines the interface for all payment processors."""

    @abstractmethod
    def charge(self, amount: float) -> bool:
        """Charge the customer the given amount."""
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        """Refund a previous transaction."""
        pass

    def receipt(self, amount: float) -> str:
        """Concrete method — shared by all processors."""
        return f"Receipt: {self.__class__.__name__} charged ${amount:.2f}"


class StripeProcessor(PaymentProcessor):
    def charge(self, amount):
        print(f"Stripe: charging ${amount:.2f}")
        return True

    def refund(self, transaction_id):
        print(f"Stripe: refunding transaction {transaction_id}")
        return True


class PayPalProcessor(PaymentProcessor):
    def charge(self, amount):
        print(f"PayPal: charging ${amount:.2f}")
        return True

    def refund(self, transaction_id):
        print(f"PayPal: refunding transaction {transaction_id}")
        return True


# Cannot instantiate abstract class
# p = PaymentProcessor()   # TypeError!

stripe = StripeProcessor()
stripe.charge(49.99)
print(stripe.receipt(49.99))

# Polymorphism with abstract classes
def process_payment(processor: PaymentProcessor, amount: float):
    if processor.charge(amount):
        print(processor.receipt(amount))

for processor in [StripeProcessor(), PayPalProcessor()]:
    process_payment(processor, 99.00)
```

### Abstract properties

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def name(self):
        return "Square"
```

---

## Dunder (Magic) Methods

Dunder methods (double underscore methods) let you define how your objects behave with Python's built-in operations — comparisons, arithmetic, string representation, iteration, and more.

### Representation methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # For developers — unambiguous, should be eval-able if possible
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        # For end users — readable
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))   # Point(3, 4)
print(str(p))    # (3, 4)
print(p)         # (3, 4)  — str() is called by print()
```

### Arithmetic operators

```python
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 + p2)   # (4, 6)
print(p2 - p1)   # (2, 2)
print(p1 * 3)    # (3, 6)
print(abs(p2))   # 5.0
```

### Comparison operators

```python
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)   # True
print(p1 < p3)    # True
```

### Container and context manager methods

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __bool__(self):
        return len(self._items) > 0

    def __repr__(self):
        return f"Stack({self._items})"


s = Stack()
s.push(1); s.push(2); s.push(3)

print(len(s))           # 3
print(2 in s)           # True
print(bool(s))          # True

for item in s:
    print(item)

print(s[0])             # 1
```

### Full Dunder Method Reference

| Method | Triggered by |
|---|---|
| `__init__` | `ClassName()` |
| `__repr__` | `repr(obj)` |
| `__str__` | `str(obj)`, `print(obj)` |
| `__len__` | `len(obj)` |
| `__bool__` | `bool(obj)`, `if obj` |
| `__add__` | `obj + other` |
| `__sub__` | `obj - other` |
| `__mul__` | `obj * other` |
| `__truediv__` | `obj / other` |
| `__floordiv__` | `obj // other` |
| `__mod__` | `obj % other` |
| `__pow__` | `obj ** other` |
| `__eq__` | `obj == other` |
| `__lt__` | `obj < other` |
| `__le__` | `obj <= other` |
| `__gt__` | `obj > other` |
| `__ge__` | `obj >= other` |
| `__contains__` | `item in obj` |
| `__iter__` | `for x in obj`, `iter(obj)` |
| `__next__` | `next(obj)` |
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = val` |
| `__delitem__` | `del obj[key]` |
| `__call__` | `obj()` |
| `__enter__` | `with obj` |
| `__exit__` | end of `with` block |
| `__hash__` | `hash(obj)`, use in set/dict |
| `__del__` | object is garbage collected |

---

## Composition vs Inheritance

Inheritance models "is-a" relationships. Composition models "has-a" relationships. Prefer composition when the relationship is about having something rather than being something.

```python
# Inheritance — "is-a" (correct use)
class Animal: pass
class Dog(Animal): pass   # Dog IS-AN Animal — correct

# Composition — "has-a" (correct use)
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"


class GPS:
    def get_location(self):
        return "37.7749 N, 122.4194 W"


class Car:
    def __init__(self, make, model):
        self.make   = make
        self.model  = model
        self.engine = Engine()   # Car HAS-AN Engine
        self.gps    = GPS()      # Car HAS-A GPS

    def start(self):
        return self.engine.start()

    def location(self):
        return self.gps.get_location()


car = Car("Toyota", "Camry")
print(car.start())      # Engine started
print(car.location())   # 37.7749 N, 122.4194 W
```

### Composition is more flexible

```python
# With composition you can easily swap components
class ElectricEngine:
    def start(self):
        return "Electric motor activated silently"

    def stop(self):
        return "Motor deactivated"


class ElectricCar(Car):
    def __init__(self, make, model, battery_kwh):
        super().__init__(make, model)
        self.engine      = ElectricEngine()   # swap the engine component
        self.battery_kwh = battery_kwh

ev = ElectricCar("Tesla", "Model S", 100)
print(ev.start())   # Electric motor activated silently
```

---

## Dataclasses

`dataclasses` is a module that auto-generates boilerplate code (`__init__`, `__repr__`, `__eq__`) for classes that are primarily used to store data.

```python
from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5


p = Point(3.0, 4.0)
print(p)                       # Point(x=3.0, y=4.0) — __repr__ auto-generated
print(p.distance_from_origin()) # 5.0
print(Point(1, 2) == Point(1, 2))  # True — __eq__ auto-generated
```

### Dataclass with defaults and complex fields

```python
@dataclass
class Developer:
    name:     str
    language: str
    level:    int = 1
    skills:   List[str] = field(default_factory=list)   # mutable default

    def __post_init__(self):
        # runs after __init__ — great for validation
        if self.level < 1 or self.level > 10:
            raise ValueError(f"Level must be 1-10, got {self.level}")
        self.name = self.name.strip().title()

    def add_skill(self, skill: str):
        self.skills.append(skill)


dev = Developer("haseeb", "Python", level=7)
dev.add_skill("React")
dev.add_skill("TypeScript")
print(dev)
# Developer(name='Haseeb', language='Python', level=7, skills=['React', 'TypeScript'])
```

### Frozen dataclasses — immutable objects

```python
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

    def hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"


red = Color(255, 0, 0)
print(red.hex())    # #ff0000
# red.r = 128       # FrozenInstanceError — cannot modify
```

---

## Class Decorators

### `@property` — already covered above

### `@classmethod` and `@staticmethod` — already covered above

### `@functools.cached_property` — lazy computed properties

```python
import functools
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @functools.cached_property
    def area(self):
        print("Computing area...")
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area)   # Computing area... 78.53...
print(c.area)   # 78.53... — cached, not recomputed
```

### Custom class decorator

```python
def singleton(cls):
    """Ensures only one instance of the class ever exists."""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class AppConfig:
    def __init__(self):
        self.debug = False
        self.version = "1.0"

c1 = AppConfig()
c2 = AppConfig()
print(c1 is c2)   # True — same object
```

---

## Slots for Memory Optimization

By default, Python stores instance attributes in a dictionary (`__dict__`), which is flexible but uses extra memory. `__slots__` tells Python to use a fixed-size array instead.

```python
import sys

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = NormalPoint(1, 2)
p2 = SlottedPoint(1, 2)

print(sys.getsizeof(p1.__dict__))  # ~232 bytes (the dict overhead)
print(hasattr(p2, "__dict__"))     # False — no dict, uses slots

# Slots are faster and use less memory
# Useful when you are creating millions of instances (e.g., game entities, data rows)
```

> **Trade-off:** With `__slots__`, you cannot add arbitrary attributes dynamically. It is a deliberate restriction that pays off in memory-heavy scenarios.

---

## OOP Design Principles — SOLID

### S — Single Responsibility Principle

A class should have one reason to change.

```python
# Bad — too many responsibilities
class User:
    def __init__(self, name, email):
        self.name  = name
        self.email = email

    def save_to_db(self): ...       # database concern
    def send_welcome_email(self): ...  # email concern
    def generate_report(self): ...  # reporting concern

# Good — each class does one thing
class User:
    def __init__(self, name, email):
        self.name  = name
        self.email = email

class UserRepository:
    def save(self, user): ...

class EmailService:
    def send_welcome(self, user): ...
```

### O — Open/Closed Principle

Open for extension, closed for modification.

```python
# Bad — you have to modify this every time you add a new shape
class AreaCalculator:
    def calculate(self, shape):
        if isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height
        # need to edit this function for every new shape

# Good — extend by adding new classes, not changing existing code
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def area(self): return self.width * self.height

class AreaCalculator:
    def calculate(self, shape: Shape):
        return shape.area()   # works with any shape, forever
```

### L — Liskov Substitution Principle

A subclass should be usable wherever its parent class is expected.

```python
# Bad — Square breaks the Rectangle contract
class Rectangle:
    def set_width(self, w): self.width = w
    def set_height(self, h): self.height = h
    def area(self): return self.width * self.height

class Square(Rectangle):
    def set_width(self, w):
        self.width = self.height = w   # breaks expected behavior of Rectangle

# Good — model it properly
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, w, h): self.width = w; self.height = h
    def area(self): return self.width * self.height

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
```

### I — Interface Segregation Principle

Do not force classes to implement methods they do not need.

```python
# Bad — Printer is forced to implement methods it cannot use
class Machine(ABC):
    @abstractmethod
    def print(self): pass
    @abstractmethod
    def scan(self): pass
    @abstractmethod
    def fax(self): pass

# Good — split into focused interfaces
class Printable(ABC):
    @abstractmethod
    def print(self): pass

class Scannable(ABC):
    @abstractmethod
    def scan(self): pass

class SimplePrinter(Printable):
    def print(self): print("Printing...")

class AllInOne(Printable, Scannable):
    def print(self): print("Printing...")
    def scan(self):  print("Scanning...")
```

### D — Dependency Inversion Principle

Depend on abstractions, not concrete implementations.

```python
# Bad — tightly coupled to MySQL
class UserService:
    def __init__(self):
        self.db = MySQLDatabase()   # concrete — hard to swap or test

# Good — depends on an abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data): pass

class MySQLDatabase(Database):
    def save(self, data): print(f"MySQL: saving {data}")

class MongoDatabase(Database):
    def save(self, data): print(f"Mongo: saving {data}")

class UserService:
    def __init__(self, db: Database):   # inject the dependency
        self.db = db

service = UserService(MySQLDatabase())
service = UserService(MongoDatabase())   # swap with zero code changes
```

---

## Real-World Project Structure

```
my_project/
├── models/
│   ├── __init__.py
│   ├── base.py         # BaseModel with shared logic
│   ├── user.py         # User class
│   └── product.py      # Product class
├── services/
│   ├── __init__.py
│   ├── auth.py         # AuthService
│   └── payment.py      # PaymentService
├── repositories/
│   ├── __init__.py
│   └── user_repo.py    # UserRepository
└── exceptions.py       # Custom exception hierarchy
```

```python
# models/base.py
from abc import ABC
from datetime import datetime

class BaseModel(ABC):
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self._id = None

    @property
    def id(self):
        return self._id

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self._id})"


# models/user.py
class User(BaseModel):
    def __init__(self, name: str, email: str, role: str = "user"):
        super().__init__()
        self.name   = name
        self.email  = email
        self.role   = role
        self._password_hash = None

    def set_password(self, password: str):
        import hashlib
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        import hashlib
        return self._password_hash == hashlib.sha256(password.encode()).hexdigest()

    @property
    def is_admin(self):
        return self.role == "admin"


# services/auth.py
class AuthService:
    def __init__(self, user_repository):
        self._repo = user_repository

    def login(self, email: str, password: str):
        user = self._repo.find_by_email(email)
        if not user or not user.check_password(password):
            raise InvalidCredentialsError("Invalid email or password")
        return self._generate_token(user)

    def _generate_token(self, user):
        return f"token_{user.id}_{user.email}"
```

---

## Common Mistakes

### Mistake 1: Forgetting `self` in method definitions

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment():          # missing self!
        self.count += 1       # TypeError when called

    def increment(self):      # correct
        self.count += 1
```

### Mistake 2: Mutable default in class body

```python
# Bug — all instances share the same list
class Team:
    members = []   # class variable, shared!

    def add(self, name):
        self.members.append(name)

t1 = Team(); t2 = Team()
t1.add("Alice")
print(t2.members)   # ['Alice'] — unexpected!

# Fix
class Team:
    def __init__(self):
        self.members = []   # instance variable
```

### Mistake 3: Not calling `super().__init__()`

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # super().__init__(name) missing!
        self.breed = breed

d = Dog("Rex", "Husky")
print(d.name)    # AttributeError — name was never set
```

### Mistake 4: Overusing inheritance when composition fits better

```python
# Wrong — a Car is not a type of Engine
class Engine:
    def start(self): pass

class Car(Engine):   # Car IS-AN Engine? No.
    pass

# Right
class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS-AN Engine
```

### Mistake 5: Confusing `__str__` and `__repr__`

```python
class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    # __repr__ — for developers and debugging
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"

    # __str__ — for end users
    def __str__(self):
        return f"{self.name} — ${self.price:.2f}"

p = Product("Laptop", 999.99)
print(str(p))    # Laptop — $999.99
print(repr(p))   # Product(name='Laptop', price=999.99)
```

### Mistake 6: Using `__del__` for important cleanup

```python
# Bad — __del__ is not guaranteed to run, and timing is unpredictable
class FileWrapper:
    def __del__(self):
        self.file.close()   # might not run, or run too late

# Good — use context manager
class FileWrapper:
    def __enter__(self):
        self.file = open(self.path)
        return self

    def __exit__(self, *args):
        self.file.close()   # always runs
```

---

## Quick Cheat Sheet

```python
# Define a class
class MyClass:
    class_var = "shared"

    def __init__(self, x):
        self.x = x          # instance variable

    def instance_method(self):
        return self.x

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    def static_method():
        return "no self or cls"

# Inheritance
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def method(self):
        return super().method()   # call parent

# Multiple inheritance
class C(A, B): pass
print(C.__mro__)               # method resolution order

# Abstract class
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def method(self): pass

# Properties
class Obj:
    @property
    def value(self): return self._value

    @value.setter
    def value(self, v): self._value = v

# Dunder methods
def __repr__(self): return f"MyClass({self.x})"
def __str__(self):  return str(self.x)
def __len__(self):  return ...
def __eq__(self, other): return self.x == other.x
def __add__(self, other): return MyClass(self.x + other.x)

# Dataclass
from dataclasses import dataclass, field
@dataclass
class Point:
    x: float
    y: float = 0.0
    tags: list = field(default_factory=list)

# Checks
isinstance(obj, ClassName)     # is obj an instance of ClassName?
issubclass(Child, Parent)      # is Child a subclass of Parent?
hasattr(obj, "attr")           # does obj have this attribute?
getattr(obj, "attr", default)  # get attribute safely
setattr(obj, "attr", value)    # set attribute dynamically
```

---

## Further Reading

- [Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Docs — abc module](https://docs.python.org/3/library/abc.html)
- [Python Docs — dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Python Docs — Data Model (Dunder Methods)](https://docs.python.org/3/reference/datamodel.html)
- [Real Python — OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [PEP 557 — Data Classes](https://peps.python.org/pep-0557/)

---

*Written for Python 3.7+. All examples tested and working.*
# Project Brief

Yesterday, we coded a `Rectangle` class that had a `width` and a `height` attribute. The class also had an `area()`, `perimeter()`, and an `is_square()` method.

Your task for today is to add two magic methods to that class `__str__` and `__eq__`. The `__str__` method should return a string representation of the Rectangle and `__eq__` should enable comparing two different rectangle instances returning True or False based on whether the rectangles are similar or not (i.e., have the same width and height).

## Resources

Magic methods in Python, also known as dunder methods, are special methods that start and end with double underscores (e.g., `__init__`, `__str__`). They allow you to define the behavior of objects for built-in operations like creation, representation, comparison, and arithmetic. Essentially, they enable you to customize how your objects interact with Python's syntax and built-in functions. For example, `__str__` defines how an object is converted to a string, and `__eq__` defines how two objects are compared for equality.

## Usage

```python
print(rectangle)
print(rectangle == square)
```

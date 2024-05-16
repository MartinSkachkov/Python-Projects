# Rectangle Class in Python

This project is a practice of object-oriented programming in Python. We are developing a class that represents a rectangle geometrical figure, similar to what you might find in a civil engineering application like AutoCAD.

## Class Definition

The `Rectangle` class has the following characteristics:

- **Instance Attributes**: The class has two instance attributes, `width` and `height`.

- **Methods**: The class has the following methods:
  - `area()`: This method returns the area of the rectangle.
  - `perimeter()`: This method returns the perimeter of the rectangle.
  - `is_square()`: This method returns `True` if the rectangle is a square and `False` (or `None`) if it is not.

## Usage

Here is a basic example of how to use the `Rectangle` class:

```python
# Create an instance of the Rectangle class
rect = Rectangle(10, 20)

# Get the area of the rectangle
print(rect.area())

# Get the perimeter of the rectangle
print(rect.perimeter())

# Check if the rectangle is a square
print(rect.is_square())
```

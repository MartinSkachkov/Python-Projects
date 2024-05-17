class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def is_square(self):
        return self.height == self.width
    
    def __str__(self) -> str:
        if self.height == 1 and self.width == 1:
            return '*'
        
        line = '*' + ' ' * (self.width - 2) + '*\n'
        rows = self.height - 2

        rectangle_str = '*' * self.width + '\n'
        rectangle_str += line * rows
        rectangle_str += '*' * self.width + '\n'

        return rectangle_str

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
    
rectangle = Rectangle(5, 10)
square = Rectangle(7, 7)

print(f'''Area: {rectangle.area()}
Perimeter: {rectangle.perimeter()}
Is_square: {rectangle.is_square()}''')

print(f'''Area: {square.area()}
Perimeter: {square.perimeter()}
Is_square: {square.is_square()}''')

#operator overloading
print(rectangle)
print(rectangle == square)
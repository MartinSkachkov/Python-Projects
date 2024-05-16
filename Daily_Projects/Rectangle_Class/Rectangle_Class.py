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
    
rectangle = Rectangle(5, 10)
square = Rectangle(7, 7)

print(f'''Area: {rectangle.area()}
Perimeter: {rectangle.perimeter()}
Is_square: {rectangle.is_square()}''')

print(f'''Area: {square.area()}
Perimeter: {square.perimeter()}
Is_square: {square.is_square()}''')
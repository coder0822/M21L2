class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create an instance of the Rectangle class
rectangle = Rectangle(length, width)

# Call the calculate_area method to find the area of the rectangle
area = rectangle.calculate_area()

# Print the calculated area of the rectangle
print("The area of the rectangle is:", area)
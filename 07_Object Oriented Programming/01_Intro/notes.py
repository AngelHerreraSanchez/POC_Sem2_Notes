# # procedural approach
# def calculate_area(width, height):
#     return width * height


# width = int(input('What is the width? '))
# height = int(input('What is the height? '))
# area = calculate_area(width, height)
# print('The area is', area)



# # object approach
class Rectangle:
    def __init__(self, width, height):
      self.width = width
      self.height = height
      

    def get_area(self):
        return self.width * self.height


a = int(input('What is the width? '))
b = int(input('What is the height? '))

rect1 = Rectangle(a, b)
print("The area of rect1 is",rect1.get_area())

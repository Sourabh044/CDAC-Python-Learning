import math
# Class Radius
class circle:
    '''Circle Object'''
    def __init__(self,radius):
        self.radius = radius
# Function Area
    def area(self):
        '''func to find area of the circle'''
        print('Area of the circle is',round(math.pi*(self.radius**2),2))
    def circumference(self):
        print('Circumference of the circle is',round(2*math.pi*r,2))

r = float(input('Enter the Radius of the Circle: '))
objCircle = circle(r) # Creating object of the circle
objCircle.area()
objCircle.circumference()
#  Class Rectangle
class rectangle:
    '''Class Rectangle'''
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        '''func to find the area of the rectangle'''
        print('Area of the Rectangle is',round((self.l*self.b),2))
l = float(input('Enter the Length of the Rectangle: '))
b = float(input('Enter the Breadth of the Rectangle: '))
objrectangle = rectangle(l,b) #Creating object of the rectangle
objrectangle.area()
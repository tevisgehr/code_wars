#https://www.codewars.com/kata/sortable-shapes/train/python
'''
cd '.\Python\TevisPrograms\Code Wars'
python
import cw16 as cw16
cw16.Square.area
'''
import math

class Shape(object):
    area = 1

class Square(Shape):
    def __init__(self, side):
        self.side = side
        self.area = side**2
    def __lt__(self,other):
        return self.area < other.area

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.area = self.width*self.height
    def __lt__(self,other):
        return self.area < other.area

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
        self.area = 0.5*base*height
    def __lt__(self,other):
        return self.area < other.area

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        self.area = math.pi*(radius**2)
    def __lt__(self,other):
        return self.area < other.area

class CustomShape(Shape):
    def __init__(self, area):
        self.area = area
    def __lt__(self,other):
        return self.area < other.area

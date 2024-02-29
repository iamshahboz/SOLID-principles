# you should do

from abc import ABC, abstractmethod 

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width 
        self.height = height

    def calculate_area(self):
        return self.width * self.height 
    
class Square(Shape):
    def __init__(self, side):
        self.side = side 

    def calculate_area(self):
        return self.side ** 2 
    
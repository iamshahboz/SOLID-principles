# you should not do
from typing import Any


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key,value)
        if key in ("width", "height"):
            self.__dict__['width'] = value
            self.__dict__['height'] = value 
            

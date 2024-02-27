from math import pi 

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == 'rectangle':
            self.width = kwargs['width']
            self.height = kwargs['height']
        elif shape_type == 'circle':
            self.radius = kwargs['radius']

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            return self.width * self.height
        elif self.shape_type == 'circle':
            return pi * self.radius ** 2 
        
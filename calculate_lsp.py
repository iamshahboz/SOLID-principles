from shapes_lsp import Square

square = Square(5)
# print(vars(square))

square.width = 7 
# print(vars(square))

square.height = 9 
# print(vars(square))

from shapes_lsp2 import Rectangle, Square

def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

print(get_total_area([Rectangle(10, 5), Square(5)]))



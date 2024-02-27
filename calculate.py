from shapes_ocp import Shape 

rectangle = Shape('rectangle', width=10, height=5)
result = rectangle.calculate_area()
# print(result)

circle = Shape('circle', radius=5)
c = circle.calculate_area()
print(c)

# Imagine that you need to add a new shape, may be a square. How would you do that?
# So the option is here to add another elif cause to __init__() and to .calculate area
# so that you can address the requirement of a square shape. Having to make these changes 
# means that your class is open for modification. That violates the open-closed principle



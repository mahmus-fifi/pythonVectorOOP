"""Tutorial on creating a vector class 
25/09/2023
@ work 

"""
class Vector2:
    """a basic vector 2 class"""
    def __init__(self, x_value = int, y_value = int):
        self.x_value = x_value
        self.y_value = y_value

    def __str__(self):
        return f'X value is: {self.x_value}, Y value is: {self.y_value}'
    # claculates the magnitude of the two vectors 
    def Mangitude(self, x_value, y_value):
        return f'The Magnitude is: {x_value **2 * y_value **2}'
    
# creating the object and instances    
vec2 = Vector2(0, 0)
vec2.x_value = 2
vec2.y_value = 9
print(vec2)
r = vec2.Mangitude(2,4)
print(r)

    


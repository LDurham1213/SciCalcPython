import math
from typing import Union
Number = Union[int,float]

class Calculator:
#status set here
    def __init__(self):
        self.display = 0

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    
    def mult(self, x, y):
        return x * y
    
    def square(self, x, y):
        return x ** y
    
    def squareroot(self, x, y=2):
        return x ** (1/y)

    

        

# add lots more methods to this calculator class.

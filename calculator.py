import math
from typing import Union

Number = Union[int,float]

class Calculator:
#status set here
    def __init__(self):
        self.display = 0

    def get_display(self):
        return self.display

    def add(self, x, y):
        self.display = x + y
        return self.display

    def sub(self, x, y):
        self.display = x - y
        return self.display
    
    def multiply(self, x, y):
        self.display = x * y
        return self.display
    
    def square(self, x):
        self.display = x ** 2
        return self.display
    
    def squareroot(self, x):
        self.display = x ** 0.5
        return self.display
    
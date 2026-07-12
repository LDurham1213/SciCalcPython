import math
from calculator import Calculator

class SciCalc(Calculator):

    def factorial(self):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        if self.display < 0:
            self.error = "Factorial requires a non-negative number"
            return self.error
        if self.display != int(self.display):
            self.error = "Factorial requries a whole number"
            return self.error
        
        self.display = math.factorial(int(self.display))
        return self.display
    
    def log(self):
        if self.hasError():
            return self.error
        
        if self.display <= 0:
            self.error = "Log undefined for zeror or negative numbers"
            return self.error
        
        self.display = math.log10(self.display)
        return self.display
    
    def inversLog(self):
        if self.hasError():
            return self.error
        
        self.display = 10 ** self.display
        return self.display
    
    def natruallLog(self):
        if self.hasError():
            return self.error
        
        if self.display <= 0:
            self.error = "Natural log undefined for zero or negative nubmers"
            return self.error
        
        self.display = math.log(self.display)
        return self.display
    
    def inverseNaturalLog(self):
        if self.hasError():
            return self.error
        self.display = math.exp(self.display)
        return self.display

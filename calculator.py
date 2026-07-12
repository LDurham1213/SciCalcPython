class Calculator:
    ERROR = "Err"

#status set here
    def __init__(self):
        self.display = 0

    def getDisplay(self):
        return self.display
    
    def hasError(self):
        return self.display == "Err"
    
    def clear(self):
        self.display = 0
        return self.display
    
    def getDisplay(self):
        return self.display
    
    def setDisplay(self,value):
        if self.hasError():
            return self.display
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            self.display = self.ERROR
        else:
            self.display = value
        return self.display

#Simple math functions
    def add(self, x, y):
        if self.hasError():
            return self.display
        
        try:
            self.display = x + y
        except (TypeError, ValueError, OverflowError):
            self.display = self.ERROR

        return self.display
        
    def subtract(self, x, y):
        if self.hasError():
            return self.display
        try:
            self.display = x - y
        except (TypeError, ValueError, OverflowError):
            self.display = self.ERROR
        return self.display
    
    def multiply(self, x, y):
        if self.hasError():
            return self.display
        try:
            self.display = x * y
        except (ZeroDivisionError, TypeError, ValueError, OverflowError):
            self.display = self.ERROR
        return self.display
    
    def divide(self, x, y):
        if self.hasError():
            return self.display
        try:
            self.display = x / y
        except (ZeroDivisionError, TypeError, ValueError, OverflowError):
            self.display = self.ERROR
        return self.display
    
    def square(self, x):
        if self.hasError():
            return self.display
        try:
            self.display = x ** 2
        except (ZeroDivisionError, TypeError, ValueError, OverflowError):
            self.display = self.ERROR
        return self.display
    
    def squareroot(self, x):
        if self.hasError():
            return self.display
        try:
            self.display = x ** 0.5
        except (ZeroDivisionError, TypeError, ValueError, OverflowError):
            self.display = self.ERROR
        return self.display
    
    def inverse(self):
        if self.hasError():
            return self.display
        try:
            # ensure numeric division even if display is a numeric string; will raise on invalid types
            self.display = 1 / float(self.display)
        except (ZeroDivisionError, TypeError, ValueError, OverflowError):
            self.display = self.ERROR
        return self.display

    def exponentiate(self, exponent):
        if self.hasError():
            return self.display
        try:
            result = self.display ** exponent
            self.display = self.ERROR if isinstance(result, complex) else result
        except (ZeroDivisionError, TypeError, ValueError, OverflowError):
            self.display = self.ERROR
        return self.display
    
    def switchSign(self):
        if self.hasError():
            return self.display
        
        if isinstance(self.display, (int, float)):
            self.display = -self.display
        else:
            self.display = self.ERROR

        return self.display

#Custom features
    def absoluteValue(self):
        if self.hasError():
            return self.display
        if isinstance(self.display, (int, float)):  #check if value is int or dec  
            self.display = abs(self.display)
        else:
            self.display = "Err"
        
        return self.display
    
    def percentage(self):
        if self.hasError():
            return self.display

        if isinstance(self.display, (int, float)):   #check if value is int or dec
            self.display = self.display / 100
        else:
            self.display = "Err"
        
        return self.display
    

# add lots more methods to this calculator class.
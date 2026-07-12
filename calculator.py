class Calculator:

    # Error Messages
    INVALID_INPUT_ERROR = "Invalid input"
    DIVIDE_BY_ZERO_ERROR = "Cannot divide by zero"
    OVERFLOW_ERROR = "Number too large"
    INVALID_EXPONENT_ERROR = "Invalid expoent"
    INVALID_OPERATION_ERROR = "Invalid operation"
 ##   ERROR = "Err"-------

#status set here
    def __init__(self):
        self.display = 0
        self.error = None
        self.memory = 0

#----------------
#Display methods
#----------------
    def getDisplay(self):
        """
        Return the error message when an error exists.
        Otherwise, return the current numeric display.
        """
        if self.hasError():
          return self.error
        
        return self.display
    
    def hasError(self):
        """
        Return True when an error message has been stored.
        """
        return self.error is not None
    
    def clear(self):
        """
        Reset both the display and the error status.
        """
        self.display = 0
        self.error = None
        return self.display
   
    def setDisplay(self, value):
        """
        Set the calculator display to a valid number.
        The calculator must be cleared before continuing 
        after an error.
        """
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(value):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
         
        self.display = value
        return self.display
    
    def isValidNumber(self, value):
        """
        Boolean values are excluded bc Python treats T / F as int
        """

        return(
            isinstance(value, (int, float))
            and not isinstance(value, bool)
        )
#---------------
#Memory methods
#---------------
    def memoryAdd(self):   #M+
        """
        Add the current display value to memory.
        Update both memory and the display.
        """
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        self.memory += self.display
        self.display = self.memory
        return self.display
    
    def memoryClear(self):    #MC
        """
        Reset memory to zero.
        Leave the current display unchanged.
        """

        if self.hasError():
            return self.error
        
        self.memory = 0
        return self.display
    
    def memoryRecall(self):     # MRC
        """
        Copy the stored memory value to the display.
        """
        if self.hasError():
            return self.error
        
        self.display = self.memory

        return self.display
    
    def memoryStore(self):
        """
        Store the current display value in memory.
        Leave the display unchanged.
        """
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        self.memory = self.display
        return self.display
    
#---------------
#Simple math functions
#---------------
    def add(self, x, y):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(x) or not self.isValidNumber(y):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        try:
            self.display = x + y
        except OverflowError:
            self.error = self.OVERFLOW_ERROR

        return self.getDisplay()
        
    def subtract(self, x, y):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(x) or not self.isValidNumber(y):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        try:
            self.display = x - y
        except OverflowError:
            self.error = self.OVERFLOW_ERROR

        return self.getDisplay()
    
    def multiply(self, x, y):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(x) or not self.isValidNumber(y):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        try:
            self.display = x * y
        except OverflowError:
            self.error = self.OVERFLOW_ERROR

        return self.getDisplay()
    
    def divide(self, x, y):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(x) or not self.isValidNumber(y):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        if y == 0:
            self.error = self.DIVIDE_BY_ZERO_ERROR
            return self.error
        
        try:
            self.display = x / y
        except OverflowError:
            self.error = self.OVERFLOW_ERROR

        return self.getDisplay()
    
    def inverse(self):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        if self.display == 0:
            self.error = self.DIVIDE_BY_ZERO_ERROR
            return self.error
        
        try:
        # ensure numeric division even if display is a numeric string; will raise on invalid types
            self.display = 1 / float(self.display)
        except OverflowError:
            self.error = self.OVERFLOW_ERROR

        return self.getDisplay()

    def exponentiate(self, exponent):
        if self.hasError():
            return self.error
                
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        if not self.isValidNumber(exponent):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        try:
            result = self.display ** exponent

            if isinstance(result, complex):
                self.error = self.INVALID_EXPONENT_ERROR
            else:
                self.display = result
                 
        except ZeroDivisionError:
            self.error = self.DIVIDE_BY_ZERO_ERROR
        except OverflowError:
            self.error = self.OVERFLOW_ERROR
        except (TypeError, ValueError):
            self.error = self.INVALID_EXPONENT_ERROR

        return self.getDisplay()
    
    def switchSign(self):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error 
        
        self.display = -self.display
        return self.display
    
#---------------
# Utility functions
#---------------
    def absoluteValue(self):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        self.display = abs(self.display)
        return self.display
         
    def percentage(self):
        if self.hasError():
            return self.error                
        
        if not self.isValidNumber(self.display):
            self.error = self.INVALID_INPUT_ERROR
            return self.error

        self.display = self.display / 100
        return self.display
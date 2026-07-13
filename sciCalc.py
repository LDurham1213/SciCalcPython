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
    
    def inverse_log(self):
        if self.hasError():
            return self.error
        
        self.display = 10 ** self.display
        return self.display
    
    def natural_log(self):
        if self.hasError():
            return self.error
        
        if self.display <= 0:
            self.error = "Natural log undefined for zero or negative nubmers"
            return self.error
        
        self.display = math.log(self.display)
        return self.display
    
    def inverse_natural_log(self):
        if self.hasError():
            return self.error
        self.display = math.exp(self.display)
        return self.display
    
#----------------
# Custom features
#----------------

# Tip Function
    def tip_calculator(self, billAmount, tipPercent):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(billAmount) or not self.isValidNumber(tipPercent):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        if billAmount < 0 or tipPercent < 0:
            self.error = "Amounts cannot be negative"
            return self.error
        
        tip = billAmount * (tipPercent /100)
        self.display = billAmount + tip

        return self.display
    
    # Convert temp
    def temperature_converter(self, temperature, conversion):
        if self.hasError():
            return self.error
        
        if not self.isValidNumber(temperature):
            self.error = self.INVALID_INPUT_ERROR
            return self.error
        
        conversion = conversion.upper()

        if conversion == "C":
            self.display = (temperature - 32) * 5 / 9

        elif conversion == "F":
            self.display = (temperature * 9 / 5) + 32

        else:
            self.error = "Use C or F"

        return self.getDisplay()
#-------------------
#Scientific Functions
#-------------------
# to switch between degrees and radians
    def getTrigMode(self):
        return self.trig_mode
    
    def switchUnitsMode(self, mode=None):
        if self.hasError():
            return self.trig_mode
        
        if mode in {"Degrees", "Radians"}:
            self.trig_mode = mode
        else:
            self.trig_mode = "Degrees" if self.trig_mode == "Radians" else "Radians"
        
        return self.trig_mode

    def sine(self):
        if self.hasError():
            return self.display
        try: #needs to be a float
            val = float(self.display)
            if self.trig_mode == "Degrees":
                val = math.radians(val)

            result = math.sin(val)

            self.display = 0.0 if abs(result) < 1e-15 else result
        except (TypeError, ValueError, OverflowError):
            self.display = self.error
        return self.display
    
    def cosine(self):
        if self.hasError():
            return self.display
        try: #needs to be a float
            val = float(self.display)
            if self.trig_mode == "Degrees":
                val = math.radians(val)

            result = math.cos(val)

            self.display = 0.0 if abs(result) < 1e-15 else result
        except (TypeError, ValueError, OverflowError):
            self.display = self.error
        return self.display
    
    def tangent(self):
        if self.hasError():
            return self.display
        try: #needs to be a float
            val = float(self.display)
            if self.trig_mode == "Degrees":
                val = math.radians(val)

            result = math.tan(val)

            self.display = 0.0 if abs(result) < 1e-15 else result #decimal places
        except (TypeError, ValueError, OverflowError):
            self.display = self.error
        return self.display
    
    def inverse_sine(self):
        if self.hasError():
            return self.display
        try:
            val = float(self.display)

            result = math.asin(val) #value error if not between -1 and 1

            if self.trig_mode == "Degrees": #convert radians back to degrees
                result = math.degrees(result)

            self.display = 0.0 if abs(result) < 1e-15 else result
        except (TypeError, ValueError, OverflowError):
            self.display = self.error
        return self.display
    
    def inverse_cosine(self):
        if self.hasError():
            return self.display
        try:
            val = float(self.display)

            result = math.acos(val) #value error if not between -1 and 1

            if self.trig_mode == "Degrees": #convert radians back to degrees
                result = math.degrees(result)

            self.display = 0.0 if abs(result) < 1e-15 else result
        except (TypeError, ValueError, OverflowError):
            self.display = self.error
        return self.display
    
    def inverse_tangent(self):
        if self.hasError():
            return self.display
        try:
            val = float(self.display)

            result = math.atan(val) #value error if not between -1 and 1

            if self.trig_mode == "Degrees": #convert radians back to degrees
                result = math.degrees(result)

            self.display = 0.0 if abs(result) < 1e-15 else result
        except (TypeError, ValueError, OverflowError):
            self.display = self.error
        return self.display
import math

from calculator import Calculator

def getNumber(message):
#ask the user for one number.
#keep asking until the user enters a valid int or dec.
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("first number? "))
    return a

def displayResult(result):
    print("Display:", result)
    print()
    
def displayMenu():
    print("Available operations:")
    print("-------------------------------")
    print("  set         - Put a number on the display")
    print("  add         - Add a number to the display")
    print("  subtract    - Subtract a number from the display")
    print("  multiply    - Multiply the display by a number")
    print("  divide      - Divide the display by a number")
    print("  square      - Raise the display to the second power")
    print("  squareroot  - Find the square root of the number on display")
    print("  power       - Raise the display to an exponent")
    print("  inverse     - Calculate 1 dividend by the display")
    print("  sign        - Switch the display between positive and negative")
    # custom functions
    print("  absolute    - Calculate the absolute value")
    print("  percentage  - Divide the display by 100")
    print("  clear       - Reset the display to 0")
    print("  show        - Show the current display")
    print("  help        - Show the available operations")
    print("  q           - Quit")
    # scientific functions
    print("  mode        - Switch trig units between Degrees and Radians")
    print("  sine        - Calculate the sine of the number on display")
    print("  cosine      - Calculate the cosine of the number on display")
    print("  tangent     - Calculate the tangent of the number on display")
    print("  asine       - Calculate the inverse sine of the number on display")
    print("  acosine     - Calculate the inverse cosine of the number on display")
    print("  atangent    - Calculate the inverse tangent of the number on display")



def performCalcLoop(calc):
    displayMenu()

    while True:
        choice = input("Operation?").strip().lower()

        if choice == "q":
            break # user types q to quit calulator.

        #when the calculator displays Err, only clear, show, help and quit allowed
        if calc.hasError() and choice not in (
            "clear", "show", "help", "q"
        ):
            print("The calculator is displaying an Error")
            print("Type 'clear' before performing another operation.")
            print()
            continue

        if choice == "set":
            number = getNumber("Number? ")
            displayResult(calc.setDisplay(number))

        elif choice == 'add':
            x, y = getTwoNumbers()
            displayResult(calc.add(x, y))
        
        elif choice == "subtract":
            x, y = getTwoNumbers()
            displayResult(calc.subtract(x, y))

        elif choice == "multiply":
            x, y = getTwoNumbers()
            displayResult(calc.multiply(x, y))

        elif choice == "divide":
            x, y = getTwoNumbers()
            displayResult(calc.divide(x, y))

        elif choice == "square":
            x = getOneNumber()
            displayResult(calc.square(x))

        elif choice == "squareroot":
            x = getOneNumber()
            displayResult(calc.squareroot(x))

        elif choice == "power":
            base = getNumber("Base number? ")
            exponent = getNumber("Exponent? ")

            calc.setDisplay(base)
            displayResult(calc.exponentiate(exponent))

        elif choice == "inverse":
            number = getNumber("Number? ")

            calc.setDisplay(number)
            displayResult(calc.inverse())

        elif choice == "sign":
            number = getNumber("Number? ")

            calc.setDisplay(number)
            displayResult(calc.switchSign())

        # custom functions

        elif choice == "absolute":
            number = getNumber("Number? ")

            calc.setDisplay(number)
            displayResult(calc.absoluteValue())
        
        elif choice == "percentage":
            number = getNumber("Number? ")

            calc.setDisplay(number)
            displayResult(calc.percentage())

        # scientific functions

        elif choice == "mode":
            new_mode = calc.switchUnitsMode()
            print(f"Trig unit mode changed to: {new_mode}")
            print()
       
        elif choice == "sine":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.sine())

        elif choice == "cosine":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.cosine())

        elif choice == "tangent":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.tangent())

        elif choice == "asine":
            number = getNumber("Number (between -1 and 1)? ")
            calc.setDisplay(number)
            displayResult(calc.inverse_sine())

        elif choice == "acosine":
            number = getNumber("Number (between -1 and 1)? ")
            calc.setDisplay(number)
            displayResult(calc.inverse_cosine())

        elif choice == "atangent":
            number = getNumber("Number (between -1 and 1)? ")
            calc.setDisplay(number)
            displayResult(calc.inverse_tangent())

        # other functions

        elif choice == "clear":
            displayResult(calc.clear())
            print(f"[ Mode: {calc.getTrigMode()} ]\n")

        elif choice == "show":
            displayResult(calc.getDisplay())
            print(f"[ Mode: {calc.getTrigMode()} ]\n")

        elif choice == "help":
            displayMenu()
        
        else:
            print("That is not a valid input.")
            print("Type 'help' to see the available operations.")
            print()

# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
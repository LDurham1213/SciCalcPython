from sciCalc import SciCalc
import math

def getNumber(message):
#ask the user for one number.
#keep asking until the user enters a valid int or dec.
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")

def getTwoNumbers():
    while True:
        try:
            a = float(input("first number? "))
            b = float(input("second number? "))
            return a, b
    
        except ValueError:
            print("Error: Please enter valid numbers")
            print()

def getOneNumber():
    a = float(input("first number? "))
    return a

def displayResult(result):
    print("Display:", result)
    print()
    
def displayMenu():
    print("-------------------------------")
    print("WELCOME TO I.B.M CALCULATOR:")
    print("Select a function")
    print("-------------------------------")
    print("  1.  set         - Put a number on the display")
    print("  2.  add         - Add a number to the display")
    print("  3.  subtract    - Subtract a number from the display")
    print("  4.  multiply    - Multiply the display by a number")
    print("  5.  divide      - Divide the display by a number")
    print("  6.  square      - Raise the display to the second power")
    print("  7.  squareroot  - Find the square root of the number on display")
    print("  8.  power       - Raise the display to an exponent")
    print("  9.  inverse     - Calculate 1 dividend by the display")
    print("  10. sign        - Switch the display between positive and negative")
    # scientific functions
    print("  11. mode        - Switch trig units between Degrees and Radians")
    print("  12. sine        - Calculate the sine of the number on display")
    print("  13. cosine      - Calculate the cosine of the number on display")
    print("  14. tangent     - Calculate the tangent of the number on display")
    print("  15. asine       - Calculate the inverse sine of the number on display")
    print("  16. acosine     - Calculate the inverse cosine of the number on display")
    print("  17. atangent    - Calculate the inverse tangent of the number on display")
    # custom functions
    print("  18. absolute    - Calculate the absolute value")
    print("  19. percentage  - Divide the display by 100")
    print("  20. factorial   - Calculate factorial")
    print("  21. log         - Base 10 logarithm")
    print("  22. invlog      - 10 raised to the display number")
    print("  23. nl          - Natural Logarithm")
    print("  24. exp         - e raised to the display number")
    print("  25. ms          - Store memory")
    print("  26. m+          - Add display to memory")
    print("  27. mc          - Clear memory")
    print("  28. mrc         - Recall memory")
    print("  29. tip         - Calculate a tip")
    print("  30. temp        - Convert temperature")
    print("-------------------------------------------------------")
    print("  clear       - Reset the display to 0")
    print("  show        - Show the current display")
    print("  help        - Show the available operations")
    print("  q           - Quit")
    print()
    
def performCalcLoop(calc):
    displayMenu()

    while True:
        choice = input("What do you want to do, pick a function? ").strip().lower()

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
            displayResult(calc.switch_sign())

        elif choice == "absolute":
            number = getNumber("Number? ")

            calc.setDisplay(number)
            displayResult(calc.absolute_value())
        
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
#----end of scientific 

        elif choice == "factorial":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.factorial())

        elif choice == "log":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.log())

        elif choice == "invlog":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.inverse_log())

        elif choice == "nl":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.natural_log())

        elif choice == "exp":
            number = getNumber("Number? ")
            calc.setDisplay(number)
            displayResult(calc.inverse_natural_log())

        elif choice == "tip":
            bill = getNumber("Bill Amount? ")
            percent = getNumber("Tip Percentage? ")
            displayResult(calc.tip_calculator(bill, percent))

        elif choice == "temp":
            temperature = getNumber("Temperature? ")
            conversion = input("Convert to (C/F)? ")
            displayResult(calc.temperature_converter(temperature, conversion))

        elif choice == "ms":
            displayResult(calc.memory_store())

        elif choice == "m+":
            displayResult(calc.memory_add())

        elif choice == "mc":
            displayResult(calc.memory_clear())

        elif choice == "mrc":
            displayResult(calc.memory_recall())

        elif choice == "clear":
            displayResult(calc.clear())

        elif choice == "show":
            displayResult(calc.getDisplay())

        elif choice == "help":
            displayMenu()
        
        else:
            print("That is not a valid input.")
            print("Type 'help' to see the available operations.")
            print()

# main start
def main():
    calc = SciCalc()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()

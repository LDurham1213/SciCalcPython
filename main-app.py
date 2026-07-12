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
    while True:
        try:
            a = float(input("first number? "))
            b = float(input("second number? "))
            return a, b
    
        except ValueError:
            print("Error: Please enter valid numbers")
            print()

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
    print("  power       - Raise the display to an exponent")
    print("  inverse     - Calculate 1 dividend by the display")
    print("  sign        - Switch the display between positive and negative")
    print("  absolute    - Calculate the absolute value")
    print("  percentage  - Divide the display by 100")
    print("  factorial   - Calculate factorial")
    print("  log         - Base 10 logarithm")
    print("  invlog      - 10 raised to the display number")
    print("  nl          - Natural Logarithm")
    print("  exp         - e raised to the display number")
    print("  ms          - Store memory")
    print("  m+          - Add display to memory")
    print("  mc          - Clear memory")
    print("  mrc         - Recall memory")
    print("  tip         - Calculate a tip")
    print("  temp        - Convert temperature")
    print("  clear       - Reset the display to 0")
    print("  show        - Show the current display")
    print("  help        - Show the available operations")
    print("  q           - Quit")
    print()
    
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
            displayResult(calc.memory_story())

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
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()

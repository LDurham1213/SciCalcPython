from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("first number"))
    return a

def displayResult(x: float):
    print(x, "\n")

def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == "sub":
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
        elif choice == "multiply":
            a, b = getTwoNumbers()
            displayResult(calc.multiply(a, b))
        elif choice == "square":
            a = getOneNumber()
            displayResult(calc.square(a))
        elif choice == "squareroot":
            a = getOneNumber()
            displayResult(calc.squareroot(a))
        elif choice == "display":
            current_val = calc.get_display()
            print(f"Current Display: {current_val}\n")
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
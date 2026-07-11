from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("first number?"))
    return a

def displayResult(x):
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
        elif choice == "mult":
            a, b = getTwoNumbers()
            displayResult(calc.mult(a, b))
        elif choice == "power":
            a, b = getTwoNumbers()
            displayResult(calc.power(a,b))
        elif choice == "squareroot":
            a = getOneNumber()
            displayResult(calc.squareroot(a))   
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()

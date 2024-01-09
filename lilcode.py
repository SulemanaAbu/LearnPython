import math
# utilizing try and catch error for the almighty formula
response = ""
solveAgain = True
while solveAgain:
    try:
        print("--Using the almighty formula of to solve quadratic equations--")
        a = int(input("Enter the coefficient of x^2: "))
        b = int(input("Enter the coefficient of x: "))
        c = int(input("Enter the value of the constant: "))

        pos = -b + math.sqrt((b * b) - (4 * a * c))
        neg = -b - math.sqrt((b * b) - (4 * a * c))

        x1 = pos / (2 * a)
        x2 = neg / (2 * a)
        print()
        print(f"Your equation is: {a: }x^2{b:+}x{c:+} ")
        print()
        print(f"The first value of x is {x1}")
        print(f"The second value of x is {x2}")
    except ValueError:
        print("Oops Something went wrong!")
        print("Enter a valid a, b or c or use factorization method")
    finally:
        print()
    response = input("Would you like to solve another equation (Y / N): ").upper()
    if response == "Y":
        solveAgain = True
    else:
        solveAgain = False
        print("Thanks for using my program!")

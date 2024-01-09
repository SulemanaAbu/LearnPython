# try catch error practice
response = ""
divideAnother = True
while divideAnother:
    print("-----------Dividing two numbers---------------")
    try:
        numerator = int(input("Enter the numerator of the fraction: "))
        denominator = int(input("Enter the denominator of the fraction: "))
        result = numerator / denominator
        print(f"{numerator} / {denominator} = {round(result, 2)}")
    except ZeroDivisionError:
        print("You can't divide by zero IDIOT!")
    except ValueError:
        print("Divide by a valid number jon !")
    finally:
        print()

    response = input("Would you like to find the result of another fraction again(Y / N): ").upper()
    if response == "Y":
        divideAnother = True
    else:
        divideAnother = False
        print("Thanks for using my program! Jah Bless")

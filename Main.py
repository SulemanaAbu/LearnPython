# If and else statements
print("Temperature conversion program")
print("_______________________________")

temp = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C or F): ")

if unit == "C":
    temp = (temp * (9 / 5)) + 32
    print(f"The temperature is {round(temp, 3)}^oF")
elif unit == "F":
    temp = (temp - 32) * (5 / 9)
    print(f"The temperature is {round(temp, 3)}^oC")
else:
    print(f"{unit} is invalid!")

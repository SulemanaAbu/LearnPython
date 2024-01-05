# Exercise
import math
print("------------------------------")
print("Hypotenuse of a right triangle")
print("-------------------------------")
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

hyp = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The hypotenuse is {round(hyp, 3)}")

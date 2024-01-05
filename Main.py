# Exercise
import math
print("--------------------------------------")
print("The almighty formula for Quadratic eqn")
print("--------------------------------------")

# 2x^2 - 5x + 3
# It is in the form ax^2 + bx + c
a = int(input("Enter the coefficient of x^2: "))
print()
b = int(input("Enter the coefficient of x: "))
print()
c = int(input("Enter the constant: "))
print()
pos = -b + math.sqrt((b * b) - (4 * a * c))
neg = -b - math.sqrt((b * b) - (4 * a * c))

print(f"The first result = {pos / (2 * a)}")
print(f"The second result = {neg / (2 * a)}")

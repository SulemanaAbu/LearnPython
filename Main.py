# Dictionaries in python
menu = {"coca cola": 1.65,
        "fried rice": 65,
        "cocktail": 12,
        "pizza": 35,
        "popcorn": 23}

cart = []
total = 0

print("----------MENU---------------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("----------MENU---------------")

while True:
    food = input("Select the food you want to buy (q or Q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print("----------YOUR TOTAL---------")
print(f"Total = ${total:.2f}")

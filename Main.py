# Shopping cart program
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy (q or Q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("------ Your Cart----------")
for food in foods:
    print(food, end=" ")
print()
for price in prices:
    total += price
print()
print(f"Your total balance is {total}")

# nested for loops

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()

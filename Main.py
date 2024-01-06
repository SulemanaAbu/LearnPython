# String methods
username = input("Enter your username: ")

if len(username) > 12:
    print("Username must be 12 characters or less")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain numbers")
else:
    print(f"Welcome {username}!")

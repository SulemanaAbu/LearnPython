# Functions in python
def create_fullname(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " "+last_name


full_name = create_fullname("salman", "isak")
print(full_name)


def add(x, y):
    return x + y


print(add(1, 4))

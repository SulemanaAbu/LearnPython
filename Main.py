# arbitrary


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="Ako loop",
              city="Accra",
              state="GA",
              zip=233)

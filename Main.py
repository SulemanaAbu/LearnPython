# arbitrary

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"Street: {kwargs.get('street')}")
    print(f"City: {kwargs.get('city')}, zip: {kwargs.get('zip')}")


shipping_label("Mr.""Sulemana Abubakar",
               street="Ako loop",
               city="Accra",
               zip=123)

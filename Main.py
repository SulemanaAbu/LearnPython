# keyword

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=233, area=245, first=549, last=6037)
print(phone_num)

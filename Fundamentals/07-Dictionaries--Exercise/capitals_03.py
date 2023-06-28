countries = input().split(", ")
capitals = input().split(", ")

countries_dict = dict(zip(countries, capitals))

for key in countries_dict:
    print(f"{key} -> {countries_dict[key]}")

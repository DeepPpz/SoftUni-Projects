countries = input().split(", ")
capitals = input().split(", ")

coun_dict = dict(zip(countries, capitals))

for key in coun_dict:
    print(f"{key} -> {coun_dict[key]}")

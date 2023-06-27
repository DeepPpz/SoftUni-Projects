movie = input()
hall_type = input()
tickets = int(input())
total_income = 0

if movie == "A Star Is Born":
    if hall_type == "normal":
        total_income = tickets * 7.50
    elif hall_type == "luxury":
        total_income = tickets * 10.50
    elif hall_type == "ultra luxury":
        total_income = tickets * 13.50

elif movie == "Bohemian Rhapsody":
    if hall_type == "normal":
        total_income = tickets * 7.35
    elif hall_type == "luxury":
        total_income = tickets * 9.45
    elif hall_type == "ultra luxury":
        total_income = tickets * 12.75

elif movie == "Green Book":
    if hall_type == "normal":
        total_income = tickets * 8.15
    elif hall_type == "luxury":
        total_income = tickets * 10.25
    elif hall_type == "ultra luxury":
        total_income = tickets * 13.25

elif movie == "The Favourite":
    if hall_type == "normal":
        total_income = tickets * 8.75
    elif hall_type == "luxury":
        total_income = tickets * 11.55
    elif hall_type == "ultra luxury":
        total_income = tickets * 13.95

print(f"{movie} -> {total_income:.2f} lv.")

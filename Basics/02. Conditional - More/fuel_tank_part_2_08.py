type = input()
litres = float(input())
club_card = input()

if type == 'Gasoline':
    if club_card == 'Yes':
        cost = litres * (2.22 - 0.18)
        if litres > 25:
            cost -= cost * 0.1
        elif litres >= 20:
            cost -= cost * 0.08
    elif club_card == 'No':
        cost = litres * 2.22
        if litres > 25:
            cost -= cost * 0.1
        elif litres >= 20:
            cost -= cost * 0.08

elif type == 'Diesel':
    if club_card == 'Yes':
        cost = litres * (2.33 - 0.12)
        if litres > 25:
            cost -= cost * 0.1
        elif litres >= 20:
            cost -= cost * 0.08
    elif club_card == 'No':
        cost = litres * 2.33
        if litres > 25:
            cost -= cost * 0.1
        elif litres >= 20:
            cost -= cost * 0.08

elif type == 'Gas':
    if club_card == 'Yes':
        cost = litres * (0.93 - 0.08)
        if litres > 25:
            cost -= cost * 0.1
        elif litres >= 20:
            cost -= cost * 0.08
    elif club_card == 'No':
        cost = litres * 0.93
        if litres > 25:
            cost -= cost * 0.1
        elif litres >= 20:
            cost -= cost * 0.08

print(f'{cost:.2f} lv.')
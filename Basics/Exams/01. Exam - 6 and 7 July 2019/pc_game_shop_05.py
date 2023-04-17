sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(sold_games):
    game = input().lower()

    if game == "hearthstone":
        hearthstone += 1
    elif game == "fornite":
        fornite += 1
    elif game == "overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone = hearthstone / sold_games * 100
fornite = fornite / sold_games * 100
overwatch = overwatch / sold_games * 100
others = others / sold_games * 100

print(f"Hearthstone - {hearthstone:.2f}%")
print(f"Fornite - {fornite:.2f}%")
print(f"Overwatch - {overwatch:.2f}%")
print(f"Others - {others:.2f}%")

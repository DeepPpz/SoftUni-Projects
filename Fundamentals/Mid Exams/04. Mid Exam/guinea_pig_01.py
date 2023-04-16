food_month = float(input()) * 1000
hay_month = float(input()) * 1000
cover_month = float(input()) * 1000
guinea_weight = float(input()) * 1000
is_enough = True

for i in range(1, 31):
    food_month -= 300

    if i % 2 == 0:
        hay_month -= food_month * 0.05
    if i % 3 == 0:
        cover_month -= guinea_weight / 3

    if food_month <= 0 or hay_month <= 0 or cover_month <= 0:
        is_enough = False
        break

if is_enough:
    food_month /= 1000
    hay_month /= 1000
    cover_month /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_month:.2f}, Hay: {hay_month:.2f}, Cover: {cover_month:.2f}.")
else:
    print("Merry must go to the pet store!")

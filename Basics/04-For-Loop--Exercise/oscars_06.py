actor_name = input()
academy_points = float(input())
count = int(input())

total_points = academy_points

for rate in range(count):
    rate_name = input()
    rate_points = float(input())
    total_points += len(rate_name) * rate_points / 2

    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!')

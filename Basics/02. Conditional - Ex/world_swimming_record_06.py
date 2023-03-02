current_record = float(input())
distance = float(input())
time_per_meter = float(input())

resistance = (distance // 15) * 12.5
total_seconds = distance * time_per_meter + resistance

if total_seconds < current_record:
    print(f'Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_seconds - current_record:.2f} seconds slower.')
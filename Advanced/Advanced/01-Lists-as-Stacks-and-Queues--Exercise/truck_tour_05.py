from collections import deque

pumps = int(input())
petrol_data = deque()
distance_data = deque()

for i in range(pumps):
    curr_pump = list(map(int, input().split()))
    petrol_data.append(curr_pump[0])
    distance_data.append(curr_pump[1])

petrol_data_copy, distance_data_copy = petrol_data.copy(), distance_data.copy()
tank_gas, index = 0, 0

while distance_data_copy:
    tank_gas += petrol_data_copy.popleft()
    distance = distance_data_copy.popleft()

    if tank_gas >= distance:
        tank_gas -= distance
    else:
        petrol_data.rotate(-1)
        distance_data.rotate(-1)
        petrol_data_copy, distance_data_copy = petrol_data.copy(), distance_data.copy()
        tank_gas = 0
        index += 1

print(index)

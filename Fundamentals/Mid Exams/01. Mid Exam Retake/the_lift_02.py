ppl_waiting = int(input())
lift = list(map(int, input().split()))

for i in range(len(lift)):
    adds = 4 - lift[i]
    lift[i] = min(4, ppl_waiting + lift[i])
    ppl_waiting -= adds
    if ppl_waiting <= 0:
        break

if ppl_waiting == 0 and min(lift) == 4:
    print(*lift, sep=' ')
elif ppl_waiting > 0 and min(lift) == 4:
    print(f"There isn't enough space! {ppl_waiting} people in a queue!")
    print(*lift, sep=' ')
else:
    print("The lift has empty spots!")
    print(*lift, sep=' ')

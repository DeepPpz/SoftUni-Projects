from collections import deque

all_portions = deque([int(x) for x in input().split(', ')])
all_stamina = deque([int(x) for x in input().split(', ')])
conquered_peaks = []
all_peaks = deque(['Vihren', 'Kutelo', 'Banski Suhodol', 'Polezhan', 'Kamenitza'])
peaks_difficulties = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70
}

curr_peak = all_peaks.popleft()

for _ in range(7):
    portion = all_portions.pop()
    stamina = all_stamina.popleft()
    result = portion + stamina

    if result >= peaks_difficulties[curr_peak]:
        conquered_peaks.append(curr_peak)
        curr_peak = all_peaks.popleft() if all_peaks else None

    if len(conquered_peaks) == 5:
        break

if len(conquered_peaks) == 5:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print('Conquered peaks:')
    print(*conquered_peaks, sep='\n')

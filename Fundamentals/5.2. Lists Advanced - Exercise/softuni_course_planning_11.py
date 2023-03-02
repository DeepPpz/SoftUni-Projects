schedule = [x for x in input().split(', ')]
command = input().split(':')

while command[0] != 'course start':
    curr_lesson = command[1]
    exercise = curr_lesson + '-Exercise'

    if command[0] == 'Add' and curr_lesson not in schedule:
        schedule.append(curr_lesson)

    elif command[0] == 'Insert' and curr_lesson not in schedule:
        idx = int(command[2])
        schedule.insert(idx, curr_lesson)

    elif command[0] == 'Remove' and curr_lesson in schedule:
        schedule.remove(curr_lesson)
        if exercise in schedule:
            schedule.remove(exercise)

    elif command[0] == 'Swap':  # + exercise
        sec_lesson = command[2]
        exercise_two = sec_lesson + '-Exercise'
        if curr_lesson in schedule and sec_lesson in schedule:
            idx_one = schedule.index(curr_lesson)
            idx_two = schedule.index(sec_lesson)
            schedule[idx_one], schedule[idx_two] = schedule[idx_two], schedule[idx_one]
            if exercise in schedule and exercise_two in schedule:
                schedule[idx_one +1], schedule[idx_two +1] = schedule[idx_two +1], schedule[idx_one +1]
            elif exercise in schedule:
                schedule.remove(exercise)
                schedule.insert(idx_two +1, exercise)
            elif exercise_two in schedule:
                schedule.remove(exercise_two)
                schedule.insert(idx_one + 1, exercise_two)

    elif command[0] == 'Exercise':
        if curr_lesson in schedule and exercise not in schedule:
            idx = schedule.index(curr_lesson) + 1
            schedule.insert(idx, exercise)
        elif curr_lesson not in schedule:
            schedule.append(curr_lesson)
            schedule.append(exercise)

    command = input().split(':')

for i in range(len(schedule)):
    print(f'{i+1}.{schedule[i]}')
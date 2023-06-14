def students_credits(*raw_data):
    courses_data = {}
    for i in range(len(raw_data)):
        curr_course = raw_data[i].split('-')
        name = curr_course[0]
        earned_credits = (int(curr_course[3]) / int(curr_course[2])) * int(curr_course[1])
        courses_data[name] = earned_credits

    total_credits = sum(courses_data.values())
    sorted_data = dict(sorted(courses_data.items(), key=lambda x: -x[1]))

    if total_credits >= 240:
        end_result = f'Diyan gets a diploma with {total_credits:.1f} credits.'
    else:
        end_result = f'Diyan needs {240 - total_credits:.1f} credits more for a diploma.'
    for (name, cred) in sorted_data.items():
        end_result += f'\n{name} - {cred:.1f}'

    return end_result

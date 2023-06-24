def gather_credits(credits_needed, *courses_data):
    enrolled_courses = []
    collected_credits = 0

    for (course, creds) in courses_data:
        if collected_credits >= credits_needed:
            break

        if course not in enrolled_courses:
            enrolled_courses.append(course)
            collected_credits += creds

    end_result = ''
    diff = credits_needed - collected_credits
    if diff <= 0:
        enrolled_courses = list(sorted(enrolled_courses))
        end_result = f'Enrollment finished! Maximum credits: {collected_credits}.\n'
        end_result += f'Courses: {", ".join(enrolled_courses)}'
    else:
        end_result = f'You need to enroll in more courses! You have to gather {diff} credits more.'

    return end_result


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

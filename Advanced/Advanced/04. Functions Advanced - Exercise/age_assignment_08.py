def age_assignment(*names, **ages):
    people_dict = {}
    for name in names:
        people_dict[name] = ages.get(name[0])

    people_dict = dict(sorted(people_dict.items(), key=lambda x: x[0]))
    result = ""

    for (person, age) in people_dict.items():
        result += f"{person} is {age} years old.\n"
    return result

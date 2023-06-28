companies_data = {}
data = input().split(" -> ")

while data[0] != "End":
    company, employee_id = data[0], data[1]

    if data[0] not in companies_data:
        companies_data[company] = []

    if employee_id not in companies_data[company]:
        companies_data[company].append(employee_id)

    data = input().split(" -> ")

for (company, employees) in companies_data.items():
    print(company)
    for emp in employees:
        print(f"-- {emp}")

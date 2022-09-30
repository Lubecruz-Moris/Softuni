companies_dict = {}
while True:
    command = input()
    if command == "End":
        break
    data = command.split(" -> ")
    company = data[0]
    employee_id = "-- " + data[1]

    if company not in companies_dict:
        companies_dict[company] = []
        companies_dict[company].append(employee_id)
    else:
        if employee_id not in companies_dict[company]:
            companies_dict[company].append(employee_id)

for item, material in companies_dict.items():
    print(f"{item}")

    joined_ids = "\n".join(material)
    print(joined_ids)
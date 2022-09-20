employees_happiness = list(map(int, input().split(" ")))
improvement_factor = int(input())
total_happiness = 0
improved_list = []
happy_count = 0
for employee in employees_happiness:
    multiplied_happiness = employee * improvement_factor
    total_happiness += multiplied_happiness
    improved_list.append(multiplied_happiness)
total_happiness = total_happiness / len(employees_happiness)
for happiness in improved_list:
    if happiness > total_happiness:
        happy_count += 1

if happy_count >= len(employees_happiness) / 2:
    print(f"Score: {happy_count}/{len(improved_list)}. Employees are happy!")

else:
    print(f"Score: {happy_count}/{len(improved_list)}. Employees are not happy!")
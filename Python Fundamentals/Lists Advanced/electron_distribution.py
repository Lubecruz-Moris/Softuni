number_of_electrons = int(input())
electrons_count = 0
electrons_list = list()
for n in range(1, number_of_electrons):
    electron = 2*n**2
    if electrons_count < number_of_electrons:
        electrons_count += electron
        electrons_list.append(electron)
    if electrons_count > number_of_electrons:
        electrons_list[-1] -= abs(electrons_count - number_of_electrons)
        break


print(electrons_list)
def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for key, value in kwargs.items():
            if name[0] == key:
                result[name] = value
                break
    sorted_result = [f"{name} is {age} years old." for name, age in
                     sorted(result.items(), key=lambda x: x[0])]
    return "\n".join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

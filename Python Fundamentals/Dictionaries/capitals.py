countries = input().split(", ")
capitals = input().split(", ")
merged_dict = dict(zip(countries, capitals))
for country, capital in merged_dict.items():
    print(f"{country} -> {capital}")
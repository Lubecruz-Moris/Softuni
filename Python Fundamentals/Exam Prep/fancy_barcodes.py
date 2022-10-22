import re
count_of_codes = int(input())
pattern = r'(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)'
for i in range(count_of_codes):
    code = input()
    result = re.match(pattern, code)
    if result is None:
        print("Invalid barcode")
    else:
        product_group = re.findall(r'\d', result.group())
        if len(product_group) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(product_group)}")

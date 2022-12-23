import os


def shopping_cart(*args):
    product_limits = {
        "pizza": 4,
        "soup": 3,
        "dessert": 2
    }
    meals_dict = {
        "pizza": [],
        "soup": [],
        "dessert": [],
    }
    for command in args:
        if command == "Stop":
            break
        meal, product = command[0], command[1]
        current_meal = meal.lower()
        if len(meals_dict[current_meal]) < product_limits[current_meal]:
            if product not in meals_dict[current_meal]:
                meals_dict[current_meal].append(product)
    if not meals_dict["pizza"] and not meals_dict["soup"] and not meals_dict["dessert"]:
        return "No products in the cart!"
    else:
        sorted_dict = [f"{key[0].upper() + key[1:]}:{os.linesep} - {f'{os.linesep} - '.join(value)}".strip(" - \n") for
                       key, value in
                       sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[1].sort(), x[0]))]

        return '\n'.join(sorted_dict).strip()


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
print(shopping_cart(
    ('Pizza', 'ham'),
    # ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))

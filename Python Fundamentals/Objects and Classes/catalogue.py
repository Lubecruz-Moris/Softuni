class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        letter_list = []
        for product in self.products:
            if first_letter.lower() in product[0].lower():
                letter_list.append(product)
        return letter_list

    def __repr__(self):
        self.products.sort()
        joined_list = "\n".join(self.products)
        return f"Items in the {self.name} catalogue:" \
               f"\n{joined_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

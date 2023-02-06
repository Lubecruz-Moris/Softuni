from abc import ABC

from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def allowed_foods(self):
        return ['Fruit', 'Vegetable']

    @property
    def weight_incremental(self):
        return 0.1


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def allowed_foods(self):
        return ['Meat', 'Vegetable']

    @property
    def weight_incremental(self):
        return 0.3


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_incremental(self):
        return 0.4


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)


    def make_sound(self):
        return "ROAR!!!"

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_incremental(self):
        return 1

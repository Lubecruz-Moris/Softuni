from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def allowed_foods(self):
        pass

    @property
    @abstractmethod
    def weight_incremental(self):
        pass

    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if self.allowed_foods is not True and food_type not in self.allowed_foods:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_incremental


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size: float):
        super(Bird, self).__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        animal_type = self.__class__.__name__

        return f"{animal_type} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region: str):
        super(Mammal, self).__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__

        return f"{animal_type} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

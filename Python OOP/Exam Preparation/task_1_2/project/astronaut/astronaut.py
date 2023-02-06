import abc


class Astronaut(abc.ABC):
    BREATHE_AMOUNT = 10

    @abc.abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value


    def breathe(self):
        self.oxygen -= self.BREATHE_AMOUNT

    def increase_oxygen(self, amount):
        self.oxygen += amount

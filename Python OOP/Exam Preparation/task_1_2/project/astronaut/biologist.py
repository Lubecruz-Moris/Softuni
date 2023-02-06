from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_UNITS = 70
    BREATHE_AMOUNT = 5
    def __init__(self, name):
        super().__init__(name, self.OXYGEN_UNITS)


b = Biologist("Pesho")


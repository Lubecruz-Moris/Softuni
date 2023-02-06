from project.animal import Animal


class Lion(Animal):
    DEFAULT_CARE_MONEY = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.DEFAULT_CARE_MONEY)
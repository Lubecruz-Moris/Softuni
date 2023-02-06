from project.animal import Animal


class Tiger(Animal):
    DEFAULT_CARE_MONEY = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.DEFAULT_CARE_MONEY)
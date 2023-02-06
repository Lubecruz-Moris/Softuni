import abc


class Horse(abc.ABC):
    HORSE_SPEED = 0
    HORSE_SPEED_INCREASE = 0
    @abc.abstractmethod
    def __init__(self,name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.HORSE_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + self.HORSE_SPEED_INCREASE >= self.HORSE_SPEED:
            self.speed = self.HORSE_SPEED
            return
        self.speed += self.HORSE_SPEED_INCREASE

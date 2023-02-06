from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    HORSE_SPEED = 140
    HORSE_SPEED_INCREASE = 3

    def __init__(self, name, speed):
        super(Thoroughbred, self).__init__(name, speed)
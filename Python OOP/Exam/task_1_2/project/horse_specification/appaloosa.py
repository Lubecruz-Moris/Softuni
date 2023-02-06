from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    HORSE_SPEED = 120
    HORSE_SPEED_INCREASE = 2

    def __init__(self, name, speed):
        super(Appaloosa, self).__init__(name, speed)
        

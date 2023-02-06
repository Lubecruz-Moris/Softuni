from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        return self.astronauts.append(astronaut)

    def remove(self, astronaut):
        return self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut


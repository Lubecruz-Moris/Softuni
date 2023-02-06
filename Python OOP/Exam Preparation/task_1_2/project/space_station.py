import os

from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self, planet_repository: PlanetRepository, astronaut_repository: AstronautRepository):
        self.planet_repository = planet_repository
        self.astronaut_repository = astronaut_repository
        self.completed_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type, name):
        type_names = list(a.__name__ for a in Astronaut.__subclasses__())
        if astronaut_type not in type_names:
            raise Exception("Astronaut type is not valid!")
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = globals()[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        [planet.items.append(i) for i in items.split(', ')]
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {planet.name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.astronauts.remove(astronaut)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def find_astronauts_by_oxygen_amount(self):
        result = []
        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda a: a.oxygen, reverse=True):
            if astronaut.oxygen > 30 and len(result) < 5:
                result.append(astronaut)

        return result

    def item_hunting(self, planet, astronauts):
        for astronaut in astronauts:
            while planet.items:
                if astronaut.oxygen < astronaut.BREATHE_AMOUNT:
                    break
                astronaut.backpack.append(planet.items.pop(-1))
                astronaut.breathe()

            if not planet.items:
                break
        if not planet.items:
            self.completed_missions += 1
            return f"Planet: {planet.name} was explored. {len(astronauts)} astronauts participated in collecting items."
        self.failed_missions += 1
        return "Mission is not completed."

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        suitable_astronauts = self.find_astronauts_by_oxygen_amount()
        print([a.oxygen for a in suitable_astronauts])
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        return self.item_hunting(planet, suitable_astronauts)

    def report(self):
        result = f"{self.completed_missions} successful missions!" + os.linesep
        result += f"{self.failed_missions} missions were not completed!" + os.linesep
        result += f"Astronauts' info:" + os.linesep
        for astronaut in self.astronaut_repository.astronauts:
            backpack_items = ', '.join(astronaut.backpack) if astronaut.backpack else "none"
            result += f"Name: {astronaut.name}" + os.linesep
            result += f'Oxygen: {astronaut.oxygen}' + os.linesep
            result += f'Backpack items: {backpack_items}' + os.linesep
        return result.strip()

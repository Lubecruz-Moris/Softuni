from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        return self.planets.append(planet)

    def remove(self, planet: Planet):
        return self.planets.remove(planet)

    def find_by_name(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet
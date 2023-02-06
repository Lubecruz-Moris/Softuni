from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository
from project.space_station import SpaceStation

a_repo = AstronautRepository()
p_repo = PlanetRepository()
s = SpaceStation(p_repo, a_repo)
s.add_astronaut("Geodesist", 'Stamat')
s.add_astronaut("Meteorologist", 'Pesho')
s.add_astronaut("Biologist", 'Asen')
s.add_astronaut("Meteorologist", "Metodi")
s.add_astronaut("Geodesist", 'St')
s.add_astronaut("Geodesist", 'Sta')
s.add_astronaut("Geodesist", 'Stam')
s.add_astronaut("Geodesist", 'Stama')

print(s.add_planet("Mercury", "Coal, moonstone, Fire"))
print(s.add_planet("Mercury", "Coal, Fire"))
print(s.add_planet("Adfy", "Charcoal, Monomurter, Space Stone, Redglow"))

print(s.retire_astronaut("Pesho"))
print(s.send_on_mission("Mercury"))
print(s.recharge_oxygen())
print(s.send_on_mission('Adfy'))
print(s.report())
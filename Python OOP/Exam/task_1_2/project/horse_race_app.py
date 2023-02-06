

from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        type_names = list(a.__name__ for a in Horse.__subclasses__())
        result, idx = self.__find_by_name(horse_name, self.horses)
        if result:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type not in type_names:
            return
        horse = globals()[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        result, idx = self.__find_by_name(jockey_name, self.jockeys)
        if result:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        result_race, result_idx = self.__find_by_race_type(race_type, self.horse_races)
        if result_race:
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey_result, jockey_idx = self.__find_by_name(jockey_name, self.jockeys)
        if not jockey_result:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        reversed_horses = list(reversed(self.horses))
        type_result, type_idx = self.__find_by_type(horse_type, reversed_horses)
        if not type_result:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if self.jockeys[jockey_idx].horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        self.jockeys[jockey_idx].horse = reversed_horses[type_idx]
        reversed_horses[type_idx].is_taken = True
        return f"Jockey {jockey_name} will ride the horse {reversed_horses[type_idx].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race_result, race_idx = self.__find_by_race_type(race_type, self.horse_races)
        if not race_result:
            raise Exception(f"Race {race_type} could not be found!")
        jockey_result, jockey_idx = self.__find_by_name(jockey_name, self.jockeys)
        if not jockey_result:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if self.jockeys[jockey_idx].horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if self.jockeys[jockey_idx] in self.horse_races[race_idx].jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        self.horse_races[race_idx].jockeys.append(self.jockeys[jockey_idx])
        return f"Jockey {jockey_name} added to the {race_type} race."



    def start_horse_race(self, race_type: str):
        race_result, race_idx = self.__find_by_race_type(race_type, self.horse_races)
        if not race_result:
            raise Exception(f"Race {race_type} could not be found!")
        if len(self.horse_races[race_idx].jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        return self.__winner_decision(self.horse_races[race_idx])

    @staticmethod
    def __find_by_name(name, repo):
        idx = -1
        for obj in repo:
            idx += 1
            if obj.name == name:
                return True, idx
        return False, idx

    @staticmethod
    def __find_by_type(type, repo):
        idx = -1
        for obj in repo:
            idx += 1
        # for obj in sorted(repo, key=lambda x: x[::-1]):
            obj_horse_type = obj.__class__.__name__
            if obj_horse_type == type and not obj.is_taken:
                return True, idx
        return False, idx
    @staticmethod
    def __find_by_race_type(race_type, horse_races):
        idx = -1
        for race in horse_races:
            idx += 1
            if race.race_type == race_type:
                return True, idx
        return False, idx

    def __winner_decision(self, race):
        highest_speed = float("-inf")
        winning_jockey = ''
        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winning_jockey = jockey
        return f"The winner of the {race.race_type} race, with a speed of {highest_speed}km/h is {winning_jockey.name}! Winner's horse: {winning_jockey.horse.name}."


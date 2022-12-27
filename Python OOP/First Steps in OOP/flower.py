class Flower:
    def __init__(self, name, water_requirements):
        self.is_happy = False
        self.name = name
        self.water_requirements = water_requirements

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"

    def water(self, amount):
        if amount >= self.water_requirements:
            self.is_happy = True



flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

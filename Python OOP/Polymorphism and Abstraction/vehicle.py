from abc import ABC, abstractmethod


class Vehicle(ABC):
    VEHICLE_FUEL_CONSUMPTION = 0

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, value):
        pass

    @abstractmethod
    def refuel(self, value):
        pass


class Car(Vehicle):
    VEHICLE_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, value):
        consumed_fuel = (self.fuel_consumption + self.VEHICLE_FUEL_CONSUMPTION) * value
        if consumed_fuel < self.fuel_quantity:
            self.fuel_quantity -= consumed_fuel
            return self.fuel_quantity

    def refuel(self, value):
        self.fuel_quantity += value
        return self.fuel_quantity


class Truck(Vehicle):
    VEHICLE_FUEL_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, value):
        consumed_fuel = (self.fuel_consumption + self.VEHICLE_FUEL_CONSUMPTION) * value
        if consumed_fuel < self.fuel_quantity:
            self.fuel_quantity -= consumed_fuel
            return self.fuel_quantity

    def refuel(self, value):
        self.fuel_quantity = self.fuel_quantity + (value * 0.95)
        return self.fuel_quantity

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)



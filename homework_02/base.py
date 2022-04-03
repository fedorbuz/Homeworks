from abc import ABC
import exceptions


class Vehicle(ABC):

    weight = 1000
    started = True
    fuel = 75
    fuel_consumption = 14  # расход в л/100 км

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel / (self.fuel_consumption / 100) > distance:
            self.fuel -= self.fuel_consumption * distance / 100
        else:
            raise exceptions.NotEnoughFuel

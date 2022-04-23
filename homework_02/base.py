from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    weight: int = 1000
    started: bool = True
    fuel: int = 75
    fuel_consumption: int = 14  # расход в л/100 км

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print('Двигатель заведен')
            else:
                raise LowFuelError
        else:
            print('Дивгатель уже заведен')

    def move(self, distance):
        if self.fuel / (self.fuel_consumption / 100) > distance:
            self.fuel -= self.fuel_consumption * distance / 100
        else:
            raise NotEnoughFuel

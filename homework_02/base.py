from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    weight: int = 1000
    started: bool = False
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
        fuel_req = self.fuel_consumption * distance / 100
        if self.fuel >= fuel_req:
            self.fuel -= fuel_req
        else:
            raise NotEnoughFuel

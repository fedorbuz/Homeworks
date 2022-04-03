from abc import ABC
import exceptions

class Vehicle(ABC):
    def __init__(self, weight=1000, started=True, fuel=75, fuel_consumption=14):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start (self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError




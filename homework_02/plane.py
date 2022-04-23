"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int = 17000

    def __init__(self, max_cargo, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        cargo += self.cargo
        if cargo <= self.max_cargo:
            self.cargo = cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo



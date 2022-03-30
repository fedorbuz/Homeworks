"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass


class CargoOverLoad(Exception):
    pass


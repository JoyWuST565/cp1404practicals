"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name: str, fuel: float = 0):
        """
        Initialise a Car instance.

        :param name: str, the name of the car
        :param fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount: float):
        """
        Add amount to the car's fuel.

        :param amount: float, amount of fuel to add
        """
        self.fuel += amount

    def drive(self, distance: float) -> float:
        """
        Drive the car a given distance.

        Drive the given distance if car has enough fuel, or drive until fuel runs out.
        Returns the distance actually driven.

        :param distance: float, intended distance to drive
        :return: float, actual distance driven
        """
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """
        Return a string representation of the car.

        :return: str, string in format 'Name, fuel=..., odometer=...'
        """
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

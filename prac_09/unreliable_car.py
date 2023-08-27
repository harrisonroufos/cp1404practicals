"""
CP1404
Prac 09
UnreliableCar class
"""
from car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability chance."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Return the distance driven for the car if the reliability is more than a random number between 0-100."""
        if self.reliability > random.randint(0, 100):
            distance_driven = super().drive(distance)
            return distance_driven

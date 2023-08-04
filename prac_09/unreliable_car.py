"""
CP1404
Prac 09
UnreliableCar class
"""
from car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability > random.randint(0, 100):
            distance_driven = super().drive(distance)
            return distance_driven

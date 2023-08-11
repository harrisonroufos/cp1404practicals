"""
CP1404
Prac 09
SilverServiceTaxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness multiplier and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip plus flagfall."""
        return super().get_fare() + self.flagfall


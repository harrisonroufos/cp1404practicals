"""
CP1404 Practical
Guitar class
Estimate: 35 minutes
Actual:    minutes
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        return self.get_age() > 50

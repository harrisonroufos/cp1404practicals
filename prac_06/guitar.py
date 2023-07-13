"""
CP1404 Practical
Guitar class
Estimate: 35 minutes
Actual:   60 minutes
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """
        Initialise a Guitar instance
        name: name of guitar
        year: year guitar was made
        cost: amount of money the guitar cost
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of name, (year made) and cost of a guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns age of guitar from 2022"""
        return 2022 - self.year

    def is_vintage(self):
        """Returns if guitar is vintage if its over 50 years old"""
        return self.get_age() > 50

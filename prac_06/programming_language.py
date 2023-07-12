"""
CP1404 Practical
ProgrammingLanguage class
Estimate: 25 minutes
Actual:
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

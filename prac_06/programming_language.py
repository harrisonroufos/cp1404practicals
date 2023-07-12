"""
CP1404 Practical
ProgrammingLanguage class
Estimate: 25 minutes
Actual:
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object"""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialise a ProgrammingLanguage instance.
        name: name of programming language
        type: if is typed dynamically or static
        reflection: True or False
        year: integer, year language was created
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determines True or False to language being dynamically typed
        if False language is Statically typed"""
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False

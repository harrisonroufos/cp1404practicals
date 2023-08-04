"""
CP1404
Prac 09
Band class
"""


class Band:
    """Musician class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty band."""
        self.name = name
        self.band = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.band})"

    def add(self, musician):
        """Add an musician to band."""
        self.band.append(musician)

    def play(self):
        """Return a string for each musician in band playing their first (or no) instrument."""
        for musician in self.band:
            print(musician.play())



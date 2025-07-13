from datetime import datetime


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """
        Initialize a Guitar with name, year and cost.

        :param name: str, the name of the guitar
        :param year: int, the year it was made
        :param cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """
        Return string representation of a Guitar.

        :return: str, formatted output for a guitar
        """
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """
        Return how old the guitar is in years.

        :return: int, age of the guitar
        """
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """
        Return True if the guitar is 50 or more years old.

        :return: bool
        """
        return self.get_age() >= 50

    def __lt__(self, other):
        """
        Less-than comparison based on year.

        :param other: Guitar, another guitar to compare to
        :return: bool, True if self is older than other
        """
        return self.year < other.year

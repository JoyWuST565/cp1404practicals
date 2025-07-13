"""
Projects
Estimate: 180 minutes
Actual:   203 minutes
"""

import datetime


class Project:
    """Represent a Project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Construct a Project instance.

        :param name: str, name of the project
        :param start_date: datetime.date, start date of the project
        :param priority: int, priority level
        :param cost_estimate: float, cost estimate in dollars
        :param completion_percentage: int, percent complete (0-100)
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """
        Return a nicely formatted string representation of the Project.

        :return: str
        """
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """
        Define less-than comparison for sorting by priority.

        :param other: Project
        :return: bool
        """
        return self.priority < other.priority

    def is_complete(self):
        """
        Return True if the project is complete (100% done).

        :return: bool
        """
        return self.completion_percentage >= 100

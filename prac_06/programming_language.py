"""
Programming Language
Estimate: 45 minutes
Actual:   58 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language with typing, reflection support, and year of appearance."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """
        Initialise a ProgrammingLanguage instance.

        :param name: Name of the programming language
        :param typing: Typing discipline (e.g., "Static", "Dynamic")
        :param reflection: Boolean indicating if reflection is supported
        :param year: Year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        """
        Determine whether the programming language is dynamically typed.

        :return: True if typing is Dynamic, False otherwise
        """
        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        """
        Return a string representation of the ProgrammingLanguage instance.

        :return: Formatted string describing the language
        """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

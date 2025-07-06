"""
Programming Language
Estimate: 45 minutes
Actual:   58 minutes
"""


from programming_language import ProgrammingLanguage


def main():
    """
    Create and display programming languages with dynamic typing.
    Also demonstrates the __str__ method and object handling.
    """
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()

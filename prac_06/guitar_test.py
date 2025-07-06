"""
Guitar
Estimate: 60 minutes
Actual:   74 minutes
"""


from guitar import Guitar


def main():
    """Test get_age and is_vintage methods of the Guitar class."""
    current_year = 2022
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 500)

    print(f"{gibson.name} get_age() - Expected {current_year - 1922}. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected {current_year - 2013}. Got {another.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


main()

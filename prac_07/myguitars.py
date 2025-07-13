from guitars import Guitar


def main():
    """Main function to manage guitar collection from CSV and user input."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    print("\nAdd your new guitars:")
    guitars.extend(get_new_guitars())

    guitars.sort()
    print("\nThese are all of the guitars sorted by year:")
    display_guitars(guitars)

    save_guitars(filename, guitars)


def load_guitars(filename):
    """
    Load guitars from a CSV file.

    :param filename: str, path to the file
    :return: list of Guitar objects
    """
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def get_new_guitars():
    """
    Prompt user to enter new guitars.

    :return: list of Guitar objects
    """
    guitars = []
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
    return guitars


def display_guitars(guitars):
    """
    Display a list of guitars with formatting.

    :param guitars: list of Guitar objects
    """
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def save_guitars(filename, guitars):
    """
    Save guitars to a CSV file.

    :param filename: str, path to the file
    :param guitars: list of Guitar objects
    """
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()

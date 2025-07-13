"""
Projects
Estimate: 180 minutes
Actual:   203 minutes
"""

import datetime
from project import Project

FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"


def main():
    """Main program to manage project tasks via a menu."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
    print(menu)

    while True:
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save = input(f"Would you like to save to {FILENAME}? ").lower()
            if save in ("yes", "y"):
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice.")
        print(menu)


def load_projects(filename):
    """
    Load projects from a tab-delimited file.

    :param filename: str
    :return: list of Project objects
    """
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            name, date_str, priority, cost, completion = line.strip().split('\t')
            date = datetime.datetime.strptime(date_str, DATE_FORMAT).date()
            projects.append(Project(name, date, int(priority), float(cost), int(completion)))
    return projects


def save_projects(filename, projects):
    """
    Save the list of projects to a file.

    :param filename: str
    :param projects: list of Project objects
    """
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime(DATE_FORMAT)}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """
    Display completed and incomplete projects sorted by priority.

    :param projects: list of Project objects
    """
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """
    Show projects starting after a given date, sorted by date.

    :param projects: list of Project objects
    """
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    filtered = [p for p in projects if p.start_date >= filter_date]
    for project in sorted(filtered, key=lambda p: p.start_date):
        print(project)


def add_project(projects):
    """
    Add a new project to the list via user input.

    :param projects: list of Project objects
    """
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """
    Update completion percentage and/or priority of a selected project.

    :param projects: list of Project objects
    """
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        completion_input = input("New Percentage: ")
        priority_input = input("New Priority: ")
        if completion_input:
            project.completion_percentage = int(completion_input)
        if priority_input:
            project.priority = int(priority_input)
    except (IndexError, ValueError):
        print("Invalid selection.")


main()

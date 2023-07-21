"""
CP1404 Practical
Project management
Estimate: 180 minutes
Actual:
"""

import datetime
from project import Project

MENU = """(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date
(A)dd new project\n(U)pdate project\n(Q)uit"""

FILE_HEADER = "Name\tStart Date	Priority\tCost Estimate\tCompletion Percentage"


def main():
    """Manage projects, load, save, add, update and filter by date."""
    projects = []
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            try:
                loaded_projects = load_file()
                for loaded_project in loaded_projects:
                    projects.append(loaded_project)
            except FileNotFoundError:
                print("File not found.")
        elif choice == "s":
            save_to_file(projects)
        elif choice == "d":
            if not projects:
                print("No projects!")
            else:
                display_projects(projects)
        elif choice == "f":
            if not projects:
                print("No projects!")
            else:
                try:
                    display_filtered_by_date_projects(projects)
                except ValueError:
                    print("Incorrect format")
        elif choice == "a":
            try:
                new_project = add_project()
                projects.append(new_project)
            except ValueError:
                print("Invalid input")
        elif choice == "u":
            if not projects:
                print("No projects!")
            else:
                try:
                    update_project(projects)
                except IndexError:
                    print("Invalid project choice")
                except ValueError:
                    print("Invalid input")
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").lower()
    save_to_file(projects)
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    """Update a project"""
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = int(input("Project choice: "))
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage != "":
        projects[project_choice].completion_percentage = int(new_percentage)
    if new_priority != "":
        projects[project_choice].priority = int(new_priority)


def add_project():
    """Add a new project"""
    print("Let's add a new project")
    name = input("Name: ")

    is_valid_input = False
    while not is_valid_input:
        try:
            start_date_string = input("Start date (dd/mm/yy): ")
            start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Invalid format")

    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percentage_complete = int(input("Percent complete: "))
    project = Project(name, str(start_date), priority, cost_estimate, percentage_complete)
    return project


def display_filtered_by_date_projects(projects):
    """Displays projects after given date"""
    try:
        date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        projects_after_date = [project for project in projects if
                               datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date]
        projects_after_date.sort()
        for project_after_date in projects_after_date:
            print(project_after_date)
    except ValueError:
        print("Invalid format")


def load_file():
    """ Loads file into projects"""
    projects = []
    file_name = input("File name: ")
    in_file = open(file_name, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    in_file.close()
    print(f"{file_name} loaded.")
    return projects


def save_to_file(projects):
    """Save projects to file"""
    try:
        file_name = input("File name to save to: ")
        out_file = open(file_name, "w")
        print(FILE_HEADER, file=out_file)
        for project in projects:
            print(
                f"""{project.name}\t{project.start_date}\t{project.priority}\t
                {project.cost_estimate:.1f}\t{project.completion_percentage}""", file=out_file)
        out_file.close()
        print(f"Saved to {file_name}.")
    except FileNotFoundError:
        print("File not found.")


def display_projects(projects):
    """Displays projects"""
    projects.sort()
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    for incomplete_project in incomplete_projects:
        print(incomplete_project)
    completed_projects = [project for project in projects if project.completion_percentage >= 100]
    print("Completed projects:")
    for completed_project in completed_projects:
        print(completed_project)


main()

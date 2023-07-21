"""
CP1404 Practical
Project management
Estimate: 120 minutes
Actual:
"""

import datetime
from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"
IN_FILE = "project.txt"
OUT_FILE = "test.txt"


def main():
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            try:
                header, projects = load_file()
            except FileNotFoundError:
                print("File not found.")
        elif choice == "s":
            save_to_file(header, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            display_filtered_by_date_projects(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").lower()
    save_to_file(header, projects)


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = int(input("Project choice: "))
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    projects[project_choice].completion_percentage = new_percentage
    projects[project_choice].priority = new_priority


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percentage_complete = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, percentage_complete))


def display_filtered_by_date_projects(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects_after_date = [project for project in projects if
                           datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date]
    for project_after_date in projects_after_date:
        print(project_after_date)


def load_file():
    """ Loads file into projects"""
    projects = []
    file_name = input("File name: ")
    in_file = open(file_name, "r")
    header = in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    in_file.close()
    print(f"{file_name} loaded.")
    return header, projects


def save_to_file(header, projects):
    file_name = input("File name to save to: ")
    out_file = open(file_name, "w")
    print(header.strip("\n"), file=out_file)
    for project in projects:
        print(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.1f}\t{project.completion_percentage}",
            file=out_file)
    out_file.close()
    print(f"Saved to {file_name}.")


def display_projects(projects):
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

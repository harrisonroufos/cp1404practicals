"""
CP1404 Practical
Project management
Estimate: 120 minutes
Actual:
"""

from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by da\n(A)dd new project\n(U)pdate project\n(Q)uit"
IN_FILE = "project.txt"
OUT_FILE = "test.txt"


def main():
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            header, projects = load_file()  # header is for when saving to file for first line
        elif choice == "s":
            save_to_file(header, projects)
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").lower()
    save_to_file(header, projects)


def load_file():
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


main()

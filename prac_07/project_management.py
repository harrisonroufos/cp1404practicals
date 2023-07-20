"""
CP1404 Practical
Project management
Estimate: 120 minutes
Actual:
"""

from project import Project

FILE_NAME = "project.txt"

projects = []
in_file = open(FILE_NAME, "r")
in_file.readline()

for line in in_file:
    parts = line.strip().split("\t")
    projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))

for project in projects:
    print(project)

in_file.close()

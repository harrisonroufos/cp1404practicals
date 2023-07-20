"""
CP1404 Practical
Project management
Estimate: 120 minutes
Actual:
"""

from project import Project

IN_FILE = "project.txt"
OUT_FILE = "test.txt"

projects = []
in_file = open(IN_FILE, "r")
header = in_file.readline()

for line in in_file:
    parts = line.strip().split("\t")
    projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))

for project in projects:
    print(project)

in_file.close()

out_file = open(OUT_FILE, "w")
print(header.strip("\n"), file=out_file)
for project in projects:
    print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.1f}\t{project.completion_percentage}", file=out_file)
out_file.close()
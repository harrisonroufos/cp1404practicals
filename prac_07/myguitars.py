"""
CP1404 Practical
my guitars
"""

from prac_06.guitar import Guitar
import csv

FILE_NAME = "guitars.csv"

guitars = []
in_file = open(FILE_NAME, "r")
reader = csv.reader(in_file)
for line in reader:
    guitars.append(Guitar([line[0]], int(line[1]), float(line[2])))

guitars.sort()

for guitar in guitars:
    print(guitar)

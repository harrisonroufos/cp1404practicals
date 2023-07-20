"""
CP1404 Practical
my guitars
"""

from prac_06.guitar import Guitar
import csv

FILE_NAME = "guitars.csv"

guitars = []
in_file = open(FILE_NAME, "r")  # Open read file
reader = csv.reader(in_file)
for line in reader:
    guitars.append(Guitar(line[0], int(line[1]), float(line[2])))
guitars.sort()
for guitar in guitars:
    print(guitar)

guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $ "))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print("")
    guitar_name = input("Name: ")

out_file = open(FILE_NAME, "w")  # Open file to save to
for guitar in guitars:
    print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

in_file.close()  # Close read file
out_file.close()  # Close file to save to

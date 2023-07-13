"""
CP1404 Practical
guitars
Estimate: 35 minutes
Actual:   60 minutes
"""
from guitar import Guitar

guitars = []

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("My guitars!")
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $ "))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    print("")
    guitar_name = input("Name: ")

max_guitar_length = max([len(guitar.name) for guitar in guitars])

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{max_guitar_length}} ({guitar.year}),"
          f" worth $ {guitar.cost:10,.2f} {vintage_string}")

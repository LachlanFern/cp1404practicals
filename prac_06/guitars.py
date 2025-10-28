"""
guitars
Estimate: 60 mins
Actual:31 mins
"""
from prac_06.guitar import Guitar
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() == True else ""
    print(f"Guitar {i}: {guitar.name:>15} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage_string}")



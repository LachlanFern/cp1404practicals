"""
guitars
Estimate: 60 mins
Actual:
"""
from prac_06.guitar import Guitar

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
           Guitar("Line 6 JTV-59", 2010, 1512.9)]

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() == True else ""



    print(f"Guitar {i}: {guitar.name:>15} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage_string}")



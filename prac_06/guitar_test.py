"""
guitar_tests
Estimate: 5 mins
Actual:4 mins
"""

from prac_06.guitar import Guitar

Gibson = Guitar("Gibson L-5 Ces", 1922, 16035.40)
print(Gibson)
Gibson_age = Guitar.get_age(Gibson)
Gibson_vintage = Guitar.is_vintage(Gibson)
print(f"Gibson L-5 CES get_age() - Expected 103. Got {Gibson_age}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {Gibson_vintage}")


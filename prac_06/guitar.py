"""
guitar
Estimate = 20 mins
Actual = 10 mins
"""

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        """Return a string representaion of a guitar instance"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Return age of guitar"""
        age = 2025 - self.year
        return age

    def is_vintage(self):
        """Return True if guitar age is greater than 50"""
        return self.get_age() >= 50



"""
CP1404 Practical
Unreliable Car
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """intitialises an unreliable car instance"""
    def __init__(self, name, fuel,  reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}"

    def drive(self, distance):
        """drives car if random number is less than reliability"""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0

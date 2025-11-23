"""
CP1404
Unreliable Car Test
"""
from prac_09.unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Jeep", 100, 30)
for i in range(1, 100):
    unreliable_car.drive(20)
    unreliable_car.add_fuel(10)
    print(unreliable_car)

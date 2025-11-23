
from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(f"The taxi is a {my_taxi.name} with {my_taxi.fuel} units of fuel and the fare is ${my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.add_fuel(40)
my_taxi.drive(100)
print(f"The taxi is a {my_taxi.name} with {my_taxi.fuel} units of fuel and the fare is ${my_taxi.get_fare()}")



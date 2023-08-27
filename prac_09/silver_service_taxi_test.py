"""
CP1404
Prac 09
silver service taxi test
"""
from silver_service_taxi import SilverServiceTaxi

my_silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
my_silver_service_taxi.drive(18)
print(f"{my_silver_service_taxi}, ${my_silver_service_taxi.get_fare()}")

my_silver_service_taxi_lambo = SilverServiceTaxi("Lambo", 100, 15)
my_silver_service_taxi_lambo.drive(20)
print(f"{my_silver_service_taxi_lambo}, ${my_silver_service_taxi_lambo.get_fare()}")

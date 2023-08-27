"""
CP1404
Prac 09
taxi simulator program
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator where you choose your taxi and drive a chosen distance with bill to date of taxi costs"""
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            display_taxis(taxis)
            current_taxi = get_valid_taxi_choice(taxis)
        elif choice == "D":
            if current_taxi is not None:
                current_taxi.start_fare()
                trip_cost = drive_taxi(current_taxi)
                bill_to_date += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi):
    """Drive taxi user entered distance"""
    drive_distance = int(input("Drive how far? "))
    if drive_distance > current_taxi.fuel:
        current_taxi.drive(current_taxi.fuel)
        trip_cost = current_taxi.get_fare()
    else:
        current_taxi.drive(drive_distance)
        trip_cost = current_taxi.get_fare()
    return trip_cost


def display_taxis(taxis):
    """Display taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_taxi_choice(taxis):
    """Get valid taxi choice"""
    try:
        taxi_choice = int(input("Choose taxi: "))
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")


main()

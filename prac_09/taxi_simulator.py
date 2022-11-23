"""
CP1404 | Carl Estranero | Taxi simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """Q)uit
C)hoose
D)rive"""

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():
    total_cost = 0

    print(MENU)
    choice = input(">>>").lower()
    while choice.lower != "q":
        if choice == "c":
            print("Taxis available")
            display_taxis(TAXIS)
            chosen_taxi = int(input("Choose taxi: "))
            try:
                current_taxi = TAXIS[chosen_taxi]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            try:
                current_taxi
            except NameError:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                total_cost += current_taxi.get_fare()
        elif choice == "q":
            break
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>>").lower()
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(TAXIS)



def display_taxis(taxis):
    """Display taxis available"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
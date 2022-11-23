"""
CP1404 Practical - Carl Estranero - Silver Service Taxi Test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():

    silver_service_taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
    print(f"{silver_service_taxi.name} has driven {silver_service_taxi.drive(18)}km. "
          f"Fare: ${silver_service_taxi.get_fare():.2f}")

main()

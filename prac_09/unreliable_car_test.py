"""
CP1404 Practical - Carl Estranero - Unreliable Car Test
"""

from unreliable_car import UnreliableCar

def main():
    barely_working = UnreliableCar("Barely Working", 200, 10)
    halfway_working = UnreliableCar("Halfway working", 200, 50)
    always_working = UnreliableCar("Always Working", 200, 100)

    for i in range(3):
        print(f"Test {i+1}")
        barely_working.drive(40)
        print(f"{barely_working}")
        halfway_working.drive(40)
        print(f"{halfway_working}")
        always_working.drive(40)
        print(f"{always_working}")

main()

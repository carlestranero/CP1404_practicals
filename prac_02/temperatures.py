"""
CP1404 | temperatures | Carl Estranero
This function will convert ceslius to fahrenheit and vice-versa.
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""




def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def convert_fahrenheit(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


print("Thank you.")

main()
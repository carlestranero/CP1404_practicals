"""
CP1404 | exceptions_demo.py | Carl Estranero
This function experiments with try statements.
Answer the following questions:
1. When will a ValueError occur?
When one of the inputs are an integer.
2. When will a ZeroDivisionError occur?
When the denominator input is a 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A while loop was implemented so whenever a 0 was the input for the denominator, it just asks them again.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero, put an integer other than 0.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
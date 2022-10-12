
def main():
    number = []
    NUMBER_OF_NUMBERS = 5

    for NUMBER_OF_NUMBERS in range(1, NUMBER_OF_NUMBERS + 1):
        numberinput = float(input(f"Number {NUMBER_OF_NUMBERS}: "))
        number.append(numberinput)

    print(f"The first number is {number[0]:,.0f}")
    print(f"The last number is {number[4]:,.0f}")
    print(f"The smallest number is {min(number):,.0f}")
    print(f"The largest number is {max(number):,.0f}")
    print(f"The average of the numbers is {sum(number)/len(number)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = str(input("Please input your username: "))

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()
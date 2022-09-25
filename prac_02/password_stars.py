"""CP1404 | password_stars | Carl Estranero
This function will output an amount of stars equal to the length of the input"""

CORRECT_PASSWORD_LENGTH = 8

def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    if len(password) >= CORRECT_PASSWORD_LENGTH:
        for i in range(len(password)):
            print("*", end='')
    else:
        print("Doesnt meet minimum")


def get_password():
    password = input("Password: ")
    return password

main()
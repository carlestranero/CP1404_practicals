password = input("Password: ")
CORRECT_PASSWORD_LENGTH = 8
if len(password) >= CORRECT_PASSWORD_LENGTH:
    for i in range(len(password)):
        print("*", end='')
else:
    print("Doesnt meet minimum")

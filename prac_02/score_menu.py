"""
CP1404 | score_menu | Carl Estranero
This function will check how good a score is and print that many stars
"""

MENU = """S - Get Score
P - Print Result
R - Print Stars
Q - Quit"""

MIN_SCORE = 0
MAX_SCORE = 100

def main():
    score = "empty"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "S":
            score = score_input()
        elif choice == "P":
            checkscore(score)
        elif choice == "R":
            print_stars(score)
        print(MENU)
        choice = input(">>> ").upper()


def print_stars(score):
    if score == "empty":
        print("No score, Please press S")
    else:
        for i in range(score):
            print("*", end='',)


def score_input():
    score = int(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def checkscore(score):
    if score == "empty":
        print("No score, press S")
    else:
        if score > 100 or score < 0:
             print("Invalid score")
        elif score < 50:
             print("Bad")
        elif score < 90:
             print("Passable")
        else:
             print("excellent")
main()
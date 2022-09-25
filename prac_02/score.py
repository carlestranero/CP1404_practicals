"""
CP1404 | score | Carl Estranero
This function will see if the score is either bad, passable or excellent.
"""
import random

def main():
    score = score_input()
    checkscore(score)
    randomscore = random_score()
    print("The random score is:", randomscore)
    checkscore(randomscore)

def checkscore(score):
    if score > 100 or score < 0:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print("excellent")


def score_input():
    score = float(input("Enter score: "))
    return score

def random_score():
    randomscore = float(random.randint(0, 100))
    return randomscore

main()



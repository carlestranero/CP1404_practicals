MIN_NUMBER = 1
MAX_NUMBER = 45
QUICK_PICKS_NUMBER_LIMIT = 6

def main():
    import random
    number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        number_list = []
        for j in range(QUICK_PICKS_NUMBER_LIMIT):
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while random_number in number_list:
                random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            number_list.append(random_number)
            number_list.sort()
        print(f"{number_list[0]:>3}{number_list[1]:>3}{number_list[2]:>3}{number_list[3]:>3}{number_list[4]:>3}")

main()
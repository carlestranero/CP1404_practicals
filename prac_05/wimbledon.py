FILENAME = "wimbledon.csv"
wimbledon_data = []
countries = set()
champion_to_victories = {}


def main():
    initial_data = open_file()
    process_data(initial_data)
    acquire_statistics()

    print("Wimbledon Champions:")
    for name, victories in champion_to_victories.items():
        print(f"{name:<10}: {victories}")

    print(f"\nThese {len(countries)} that won Wimbledon:")
    print(f"{', '.join(countries)}")


def acquire_statistics():
    for line in wimbledon_data:
        countries.add(line[1])
        if line[2] in champion_to_victories:
            champion_to_victories[line[2]] += 1
        else:
            champion_to_victories[line[2]] = 1


def process_data(initial_data):
    for line in initial_data:
        line = line.strip('\n').split(',')
        wimbledon_data.append(line)


def open_file():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        initial_data = in_file.readlines()
    return initial_data


main()

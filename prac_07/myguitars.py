from prac_06.guitar import Guitar

def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year,Cost
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # Construct a Guitar object using the elements
        # year should be an int, cost should be a float
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()


    guitars.sort()
    for guitar in guitars:

        print(guitar)


main()
"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    get_data()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    organised_list_of_data = []
    for line in input_file:
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        organised_list_of_data.append(parts)
        print(organised_list_of_data)
    details_printer(organised_list_of_data)
    input_file.close()

def details_printer(organised_list_of_data):
    input_file = open(FILENAME)
    for line in range(len(organised_list_of_data)):
        print(f"{organised_list_of_data[line][0]} is taught by {organised_list_of_data[line][1]} and has {organised_list_of_data[line][2]} students")
    input_file.close()

main()
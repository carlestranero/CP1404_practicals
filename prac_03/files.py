"""CP1404 | files.py | Carl Estranero
This function reads and writes to multiples files in 1 task."""

OUTPUT_FILE = "name.txt"
total = 0
# Q1
name = str(input("Enter your name: "))
out_file = open(OUTPUT_FILE, 'w')
print(f"{name}", file=out_file)
out_file.close()

#Q2
in_file = open(OUTPUT_FILE)
text = in_file.read()
in_file.close()
print(f"Your name is {text}")

#Q3
in_file = open("numbers.txt")
total += int(in_file.readline())
total += int(in_file.readline())
print(f"The total of the first two numbers are: {total}")
in_file.close()

#Q4
total = 0
in_file = open("numbers.txt")
for line in in_file:
    total += int(line)
print(f"the total of all numbers are: {total}")
in_file.close()



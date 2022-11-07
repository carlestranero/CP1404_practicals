from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    guitar_name = input("Name: ")

print("... snip ...")
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage_string}")






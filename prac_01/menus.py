name = input("Enter name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")
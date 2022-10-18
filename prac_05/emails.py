"""
Emails
Estimate: 30 minutes
Actual:
"""

name_to_email = {}

email = input("Email: ")


while email != "":
    name_from_email = " ".join(email.split("@")[0].title().split("."))
    is_name_correct = input(f"Is your name {name_from_email}? (Y/n)")

    if is_name_correct.lower() == "y" or is_name_correct == "":
        name_to_email[name_from_email] = email
    else:
        ask_for_name = input("Name: ")
        name_to_email[ask_for_name] = email
    email = input("Email: ")

for name, email in name_to_email.items():
    print(f"{name}  ({email})")


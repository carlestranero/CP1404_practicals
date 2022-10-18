"""
CP1404/CP5632 Practical
This is a program that allows you to look up hexadecimal colour codes like those at http://www.color-hex.com/color-names.html
"""
NAME_TO_HEX = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "alice blue": "#f0f8ff",
               "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
               "amethyst": "#9966cc", "apricot": "#fbceb1", "aqua": "#00ffff", "aquamarine1": "#7fffd4"}

name = input("Enter colour name: ").lower()
while name != "":
    try:
        print(NAME_TO_HEX[name])
    except KeyError:
        print("Invalid colour name")
    name = input("Enter colour name: ").lower()

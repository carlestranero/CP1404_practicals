"""
Word Occurrences
Estimate: 20 minutes
Actual: 31 minutes
"""
text = sorted(input("Please enter any text: ").lower().split())

dictionary = {}
for i in text:
    dictionary[i] = text.count(i)

width = len(max(dictionary, key=len))
for text, frequency in dictionary.items():
    print(f"{text:{width}} : {frequency}")

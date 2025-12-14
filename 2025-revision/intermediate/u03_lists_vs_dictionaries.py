# Create a list of names.
# Create a dictionary where each name maps to a number (for example: score, rating, or age).
# Loop through the list.
# For each name, print the name and its value from the dictionary.
# Only print entries where the value is greater than 18.

names = ["Lorand", "Vance", "David", "Dad", "Grandpa"]
age = {"Lorand":15, "Vance": 13, "David": 11, "Dad":56, "Grandpa":85}     #not real

for v in names:
    if age[v] >= 35:
        print(f"{v} can drive a car, because he is {age[v]} years old.")

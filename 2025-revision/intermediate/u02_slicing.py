# Write 4–5 lines of Python that:
# Take a list of animal names
# Print only the ones that start with the letter "c"
# Then print the reversed list using slicing
# Then print the middle portion (slice from index 1 to second-to-last)

animals = ["crocadile", "elefant", "aligator", "fox", "cat", "dog"]

for v in animals:
    if v[0:1] == "c":
        print(v)

print(animals[::-1])

print(animals[1:-1])

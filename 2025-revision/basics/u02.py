# the age of the user is givin    #ask the user for their age,
# uses if/elif/else to classify them as
# “Child” (0–12),
# “Teen” (13–17),
# “Adult” (18+),
# then prints the correct category.


import random

age = random.randint(0, 30)

if age <= 12:
    print("You are a child. Parental guidence only!")
elif age <= 17:
    print("You are a teen.")
else:
    print("You are an adult.")

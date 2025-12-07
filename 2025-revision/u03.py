# Stores a number of correct answers and incorrect answers in variables
# Calculates a score using a formula of your choice (must use arithmetic operators)
# Prints a message based on the score using an if/elif/else statement
# Uses at least one function call (such as len() or print())

import random

num_answers = 24
correct_answers = random.randint(0, num_answers)
incorrect_answers = num_answers - correct_answers
score = correct_answers - (incorrect_answers / 2)

if score == num_answers:
    print("Excellent!")
elif score >= num_answers * 0.8:
    print("Great!")
elif score >= num_answers * 0.6:
    print("Good!")
elif score >= num_answers * 0.4:
    print("Fine!")
elif score >= num_answers * 0.2:
    print("Bad!")
else:
    print("Idiot!")

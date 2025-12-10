# Imports the random module
# Creates a list of 5 random numbers from 1 to 10
# Prints each number with the message: "Random number: X"
# Prints the sum of all numbers

import random

def random_numbers(n, max_value):
    numbers = []
    for i in range(n):
        x = random.randint(1, max_value)
        numbers.append(x)
        print(f"Random number: {x}")
    print(f"Sum of the numbers is {sum(numbers)}.")


random_numbers(5, 10)
random_numbers(2, 6)

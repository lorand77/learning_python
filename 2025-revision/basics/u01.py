# Defines a function double_plus_ten(x) that returns 2 * x + 10.
# Calls this function with the value 7 and stores the result in a variable called result.
# Prints result.
# Prints True if result is greater than 20, otherwise prints False.

def double_plus_ten(x):
    return 2 * x + 10

result = double_plus_ten(7)
print(result)
if result > 20:
    print(True)
else:
    print(False)


# Stores a number in a variable representing how many pages you read per day.
# Calculates how many pages that equals in a 30-day month.
# Prints a message like: "You read ___ pages per month!" using string concatenation.
# Prints whether the monthly total is greater than 100 using an if/else statement.

pages_per_day = 9
pages_per_month = pages_per_day * 30
print("You read " + str(pages_per_month) + " pages per month!")

if pages_per_month > 100:
    print("You read more than 100 pages a month!")
else:
    print("Read more!")

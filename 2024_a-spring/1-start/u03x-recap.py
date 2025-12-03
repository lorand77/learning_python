# variables, assignment, literals, operators, expressions, function calls

score = 95
score = 96
score2 = score
grade = "A"
grade2 = grade
is_finished = True

ex_correct = 20
ex_incorrect = 3
ex_missed = 2
ex_total = ex_correct + ex_incorrect + ex_missed
score = 4*ex_correct - ex_incorrect + ex_total + len("abc")
score2 = 5*ex_correct + ex_missed
print(score)
print(score2)

banner = "Welcome to the Python course!\n" * 3
print(banner)

banner_length = len(banner)*10
print(banner_length)

score = 3
great_compound_number = 909090909090909091 * 1111111111111111111
print(great_compound_number)

score2 = score


# conditionals
score = 44
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 45:
    grade = "D"
else:
    grade = "F"
print(grade)
if score >= 100:
    print("Perfect score!")

# indentation: conditionals (if), loops (for, while), function definitions

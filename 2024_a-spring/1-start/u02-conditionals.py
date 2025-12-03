
# conditionals, if-blocks, if-else blocks, branches

score = 95
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 30:
    grade = "D"
else:
    grade = "F"
print(grade)

# write the same as above with nested conditionals
if score >= 90:
    grade = "A"
else:
    if score >= 70:
        grade = "B"
    else:
        if score >= 50:
            grade = "C"
        else:
            if score >= 30:
                grade = "D"
            else:
                grade = "F"
print(grade)

if score >= 70:
    if score >= 90:
        grade = "A"
    else:
        grade = "B"
else:
    if score >= 50:
        grade = "C"
    else:
        if score >= 30:
            grade = "D"
        else:
            grade = "F"
print(grade)        



if score >= 50:
    grade_pass = "Yes"
else:
    grade_pass = "No"
print(grade_pass)



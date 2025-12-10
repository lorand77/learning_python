#function that gets unique elementd from a list

def uniq(x):
    x_uniq = []
    for v in x:
        if v not in x_uniq:
            x_uniq.append(v)
    return x_uniq


numbers = []
print(uniq(numbers))
numbers = [1, 2, 7, 32, 2, 81, 1]
print(uniq(numbers))
numbers = [1, 1.0, 1., 1.00, "1", "1.", "1.0", "A", "a"]
print(uniq(numbers))

# Write three functions:
# 1. add_prefix(word, prefix)
# Returns a new string formed by attaching the prefix to the word.
# Example: add_prefix("happy", "un") → "unhappy"
# 2. emphasize(word)
# Returns the word with "!!!" added to the end.
# Example: emphasize("wow") → "wow!!!"
# 3. process(word, prefix)
# Does not build the final string itself.
# Instead, it must:
# Call add_prefix(word, prefix)
# Then pass the result to emphasize
# And return the final result

def add_prefix(word, prefix):
    return prefix + word

def emphasize(word):
    return word + "!!!"

def process(word, prefix):
    return emphasize(add_prefix(word, prefix))

print(process("legal", "il"))

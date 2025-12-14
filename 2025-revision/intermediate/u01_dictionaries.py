# Creates a dictionary of three fruits and their prices
# Increases the price of one fruit
# Prints all fruits whose price is greater than 2 using a loop
# (You must use dictionary iteration)

fruit_prices = {"apple" :0.99, "banana":1.99, "coconut":3.99, "date":2.99}

fruit_prices["apple"] = fruit_prices["apple"] * 1.15

for k,v in fruit_prices.items():
    if v > 2:
        print(f"An {k} costs ${v}.")

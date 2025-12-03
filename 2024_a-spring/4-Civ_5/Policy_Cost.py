def round_to_5(x):
    return int(x / 5) * 5


def cum_sum(lst):
    result = []
    total = 0
    for i in lst:
        total += i
        result.append(total)
    return result

def main():
    n = 13
    num_of_city = 8
    costs = []
    for num_pol in range(n):
        base_cost = (3 * num_pol) ** 2.01 + 25
        add_cost = base_cost * 0.1 * (num_of_city - 1)
        total_cost = base_cost + add_cost
        costs.append(round_to_5(total_cost))
    print(costs)
    print(cum_sum(costs))

main()
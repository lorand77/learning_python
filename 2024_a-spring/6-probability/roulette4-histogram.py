import random
import matplotlib.pyplot as plt
from collections import Counter

N = 10000
money_end = []
n_win = 0
n_total_loss = 0

for k in range(N):
    money_initial = 1000
    money = money_initial
    bet = 1
    n_turns = 300
    for i in range(n_turns):
        # if random.randint(1,38) == 1:
        #     money += bet * 35
        # if random.randint(1,38) <= 12:
        #     money += bet * 2   
        if random.randint(1,38) <= 18:
            money += bet
            bet = 1
        else:
            money -= bet
            bet *= 2
            if bet > money:
                bet = money
        if money<=0:
            break
    money_end.append(money)

for v in money_end:
    if v > money_initial:
        n_win += 1
    if v == 0:
        n_total_loss += 1
print(f"prob win={n_win / N}  prob total loss={n_total_loss/N}   average money end={sum(money_end) / N}")

# print(Counter(money_end))

#plt.hist(money_end)
plt.hist(money_end, bins=range(min(money_end),max(money_end),10))
plt.show()
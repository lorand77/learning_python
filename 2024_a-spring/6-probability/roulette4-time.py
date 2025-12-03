import random
import matplotlib.pyplot as plt
from collections import Counter

money = 1000
bet = 1
n_turns = 300
money_history = []
bet_history = []
money_history.append(money)
for i in range(n_turns):
    bet_history.append(bet)
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
    money_history.append(money)
    if money<=0:
        break


plt.plot(money_history)
plt.show()

plt.plot(bet_history)
plt.show()
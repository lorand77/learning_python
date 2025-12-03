import random
import matplotlib.pyplot as plt

money = 100
bet = 1
n_turns = 10000

money_history = []
money_history.append(money)

for i in range(n_turns):
    if random.randint(1,38) == 1:
        money += bet * 35
    # if random.randint(1,38) <= 18:
    #     money += bet    
    else:
        money -= bet
    money_history.append(money)
    if money<=0:
        break    

#plt.plot(money_history, marker='.')
plt.plot(money_history)
plt.show()

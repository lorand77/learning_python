import random
import matplotlib.pyplot as plt

p_win = 8/36+2*(1/36+8/(36*5)+25/(36*11))
print(f"prob win={p_win*100}   house edge={((1-p_win)-p_win)*100}")


money = 100
bet = 1
n_turns = 300

money_history = []
money_history.append(money)

for i in range(n_turns):
    step1_roll = random.randint(1,6) + random.randint(1,6) 
    if step1_roll == 7 or step1_roll == 11:
        money += bet
    elif step1_roll == 2 or step1_roll == 3 or step1_roll == 12: 
        money -= bet
    else:
        while True:
            step2_roll = random.randint(1,6) + random.randint(1,6) 
            if step1_roll == step2_roll:
                money += bet
                break
            elif step2_roll == 7:
                money -= bet
                break
    money_history.append(money)
    if money<=0:
        break    

#plt.plot(money_history, marker='.')
plt.plot(money_history)
plt.show()

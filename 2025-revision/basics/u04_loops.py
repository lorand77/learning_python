# You have a list of player scores: [5, 12, 8, 7].
# Use a loop to add 3 bonus points to each score and store the results in a new list.
# Then, use a loop to print “Player X: Y points” for each updated score, where X is the player number starting from 1.

players_score = [5, 12, 8, 7]
players_new_score = []
for v in players_score:
    players_new_score.append(v + 2)

i = 0
while i < 4:
    print("Player " + str(i) + ": " + str(players_new_score[i]) + " points.")
    i += 1

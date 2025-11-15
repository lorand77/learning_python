
text = "In Civilization V the frigate is a powerful ranged naval unit in the Renaissance era. The frigate can reach further destinations fast because it can enter deep ocean tiles and it has a movement of 5 hexes per turn. In addition, the frigate has a ranged combat strength of 28 (and  25 for defense), therefore it is very effective against land and naval units. Furthermore, frigates are very useful in conquering cities because of their combat strength and that multiple frigates can surround the city and can fire at it at the same time. On the other hand, the production cost is higher than any other unit in the Renaissance era and it consumes 1 iron, which is a strategic resource that is sometimes scarce. In summary, the frigate is a powerful ranged naval unit that is a game-changer in  Renaissance warfare."
print(text,"\n")

text = text.replace(",","")
text = text.replace(".","")
words = text.split()
print(words,"\n")

print(type(words))
print(words[0])
print(words[1])
print(words[-1])

long_words = []
for v in words:
    if len(v) > 6:
        long_words.append(v)
print(long_words)


from simple_substitution_cipher import *

secret_key = "DLMXYRKNOPZASTGFEQHIJBUVWC"
plain_text = """Civilization V is a turn-based video game where you build a civilization and you compete against other civilizations. The goal of the game is to win by domination (to conquer all the capitals) or other ways (science, culture etc).
Similar to board games the world is made of hexes (hexagonal tiles). They are 3 types of hexes: land, water and ice. Land tiles can be grassland, plains, hills, forests, jungle, mountains, desert, oasis, tundra and snow. The game can have a randomly generated map or it can have an Earth map. A player can build cities, which take up that hex and the surrounding hexes. Citizens (the city’s population) work the tiles within the city’s borders and produce food, production, gold, culture and science. Food is needed to grow the city’s population,  production is needed to build things (military units, buildings and wonders), gold is needed to maintain units, buildings and for purchasing items. Culture is used to gain social policies and growing your cities’ borders, science is used to gain new technologies.
The cities can build buildings, which give yields to the city (e.g. the market gives +2 gold and 25% more gold, or the workshop gives +2 production and 10% more production). The player can also build wonders, which can be built in one city and by only one civilization. It can have several benefits, for example the Great Library gives a free library in the city it was built, a free technology, +3 science and +1 Great Scientist points, or the Notre Dame gives +10 happiness.  The player can also build national epics, which can be built in only one city but by all civilizations, for example Circus Maximus gives +5 happiness.
The cities can also build military units, which can be used to attack and conquer other cities and civilizations and to defend against other civilizations and barbarians. Military units can be melee, ranged, naval (ranged) or air (ranged) units. Melee units can only attack units on adjacent hexes and ranged units have a range how far they can shoot (typically a range of 2). Military units have a combat strength (a number) which they use to attack and defend against enemy units. For example, the swordsman has a combat strength of 11. Ranged and naval units have a separate combat strength for ranged attack and defense.  For example, the archer has a combat strength of 4 (used for defending) and a ranged combat strength of 6 (used for attacking). Air units are based in cities, can attack enemy units in their range and they attack and defend with their combat strength. For example, the bomber has a range of 10 and a combat strength of 50.  Military units (except air units) have a movement number of how many hexes they can move in 1 turn. Naval units can only move in water hexes. Land units are slowed down in rough terrain (hills, forests, jungle), in crossing rivers and cannot pass through mountains.
In Civilization 5 combat works as follows. Units and cities have health points, which is a number between 0 and 10, which represents the unit’s health. If a melee unit attacks another unit or a city then the game calculates the damage to each unit. The damage depends on their combat strength, the terrain (e.g. hills +20% strength), promotions and special modifiers (e.g. great general nearby +15% combat strength). If a unit takes damage then the health points get lower. If the health points reach 0 then the unit is killed or the city is conquered. If the defender is killed then the attacker takes its place (in case of cities are taken, the attacker moves into the city)."""
cipher_text = encrypt_simple_substitution(plain_text, secret_key)
print(cipher_text)

# brute force:
# import math
# print(float(math.factorial(26)))

# decrypted_text = decrypt_simple_substitution(cipher_text, key)
# print(decrypted_text)


from collections import Counter
print(Counter(cipher_text.lower()))


# e -> y                      

print(Counter(cipher_text.split()))

# a -> d
# and -> dtx
# the -> iny

# can -> mdt

# 'y': 313,   <- e
# 'd': 264,   <- a  
# 'i': 258,   <- t
# 'o': 239,   <- i
# 't': 231,   <- n
# 'h': 173,   <- s
# 'g': 166,   <- o
# 'q': 148,   <- r
# 'n': 130,   <- h
# 'm': 118,   <- c
# 'x': 114,   <- d
# 'a': 110,   <- l

# is -> oh


# a -> d
# b -> 
# c -> m
# d -> x
# e -> y
# f -> 
# g -> 
# h -> n
# i -> o
# j -> 
# k -> 
# l -> a
# m -> 
# n -> t
# o -> g
# p -> 
# q -> 
# r -> q
# s -> h
# t -> i
# u -> 
# v -> 
# w -> 
# x -> 
# y -> 
# z -> 

#           ABCDEFGHIJKLMNOPQRSTUVWXYZ
alphabet = "L..A..OST...CHI.R..N...DE."
alphabet = "LVZAQPOSTUGBCHIJRFMNWXYDEK"
key      = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += alphabet.lower()
key += key.lower()
reverse_substitution_table = str.maketrans(key, alphabet)
decrypted_text= cipher_text.translate(reverse_substitution_table)
print(decrypted_text)


# In Ci.ili.ation 5 co..at .or.s as .ollo.s. .nits and cities ha.e health .oints, .hich is a n...er .et.een 0 and 10, .hich re.resents the .nit’s health. I. a .elee .nit attac.s another .nit or a cit. then the .a.e calc.lates the da.a.e to each .nit. The da.a.e de.ends on their co..at stren.th, the terrain (e... hills +20% stren.th), .ro.otions and s.ecial .odi.iers (e... .reat .eneral near.. +15% co..at stren.th). I. a .nit ta.es da.a.e then the health .oints .et lo.er. I. the health .oints reach 0 then the .nit is .illed or the cit. is con..ered. I. the de.ender is .illed then the attac.er ta.es its .lace (in case o. cities are ta.en, the attac.er .o.es into the cit.).
# In Civili.ation 5 co..at wor.s as .ollows. Units and cities have health points, which is a nu..er .etween 0 and 10, which represents the unit’s health. I. a .elee unit attac.s another unit or a cit. then the .a.e calculates the da.a.e to each unit. The da.a.e depends on their co..at stren.th, the terrain (e... hills +20% stren.th), pro.otions and special .odi.iers (e... .reat .eneral near.. +15% co..at stren.th). I. a unit ta.es da.a.e then the health points .et lower. I. the health points reach 0 then the unit is .illed or the cit. is con.uered. I. the de.ender is .illed then the attac.er ta.es its place (in case o. cities are ta.en, the attac.er .oves into the cit.).
# In Civilization 5 combat works as .ollows. Units and cities have health points, which is a number between 0 and 10, which represents the unit’s health. I. a melee unit attacks another unit or a cit. then the .ame calculates the dama.e to each unit. The dama.e depends on their combat stren.th, the terrain (e... hills +20% stren.th), promotions and special modi.iers (e... .reat .eneral nearb. +15% combat stren.th). I. a unit takes dama.e then the health points .et lower. I. the health points reach 0 then the unit is killed or the cit. is con.uered. I. the de.ender is killed then the attacker takes its place (in case o. cities are taken, the attacker moves into the cit.).
# In Civilization 5 combat works as follows. Units and cities have health points, which is a number between 0 and 10, which represents the unit’s health. If a melee unit attacks another unit or a city then the .ame calculates the dama.e to each unit. The dama.e depends on their combat stren.th, the terrain (e... hills +20% stren.th), promotions and special modifiers (e... .reat .eneral nearby +15% combat stren.th). If a unit takes dama.e then the health points .et lower. If the health points reach 0 then the unit is killed or the city is con.uered. If the defender is killed then the attacker takes its place (in case of cities are taken, the attacker moves into the city).
# In Civilization 5 combat works as follows. Units and cities have health points, which is a number between 0 and 10, which represents the unit’s health. If a melee unit attacks another unit or a city then the game calculates the damage to each unit. The damage depends on their combat strength, the terrain (e.g. hills +20% strength), promotions and special modifiers (e.g. great general nearby +15% combat strength). If a unit takes damage then the health points get lower. If the health points reach 0 then the unit is killed or the city is con.uered. If the defender is killed then the attacker takes its place (in case of cities are taken, the attacker moves into the city).
# Ot Moboaocdiogt 5 mgsldi ugqzh dh rgaaguh. Jtoih dtx moioyh ndby nydain fgotih, unomn oh d tjslyq lyiuyyt 0 dtx 10, unomn qyfqyhytih iny jtoi’h nydain. Or d syayy jtoi diidmzh dtginyq jtoi gq d moiw inyt iny kdsy mdamjadiyh iny xdsdky ig ydmn jtoi. Iny xdsdky xyfytxh gt inyoq mgsldi hiqytkin, iny iyqqdot (y.k. noaah +20% hiqytkin), fqgsgiogth dtx hfymoda sgxoroyqh (y.k. kqydi kytyqda tydqlw +15% mgsldi hiqytkin). Or d jtoi idzyh xdsdky inyt iny nydain fgotih kyi aguyq. Or iny nydain fgotih qydmn 0 inyt iny jtoi oh zoaayx gq iny moiw oh mgtejyqyx. Or iny xyrytxyq oh zoaayx inyt iny diidmzyq idzyh oih fadmy (ot mdhy gr moioyh dqy idzyt, iny diidmzyq sgbyh otig iny moiw).

# The cities can also build military units, which can be used to attack and conquer other cities and civilizations and to defend against other civilizations and barbarians. Military units can be melee, ranged, naval (ranged) or air (ranged) units. Melee units can only attack units on ad.acent he.es and ranged units have a range how far they can shoot (typically a range of 2). Military units have a combat strength (a number) which they use to attack and defend against enemy units. For e.ample, the swordsman has a combat strength of 11. Ranged and naval units have a separate combat strength for ranged attack and defense.  For e.ample, the archer has a combat strength of 4 (used for defending) and a ranged combat strength of 6 (used for attacking). Air units are based in cities, can attack enemy units in their range and they attack and defend with their combat strength. For e.ample, the bomber has a range of 10 and a combat strength of 50.  Military units (e.cept air units) have a movement number of how many he.es they can move in 1 turn. Naval units can only move in water he.es. Land units are slowed down in rough terrain (hills, forests, .ungle), in crossing rivers and cannot pass through mountains.
# Iny moioyh mdt dahg ljoax soaoidqw jtoih, unomn mdt ly jhyx ig diidmz dtx mgtejyq ginyq moioyh dtx moboaocdiogth dtx ig xyrytx dkdothi ginyq moboaocdiogth dtx ldqldqodth. Soaoidqw jtoih mdt ly syayy, qdtkyx, tdbda (qdtkyx) gq doq (qdtkyx) jtoih. Syayy jtoih mdt gtaw diidmz jtoih gt dxpdmyti nyvyh dtx qdtkyx jtoih ndby d qdtky ngu rdq inyw mdt hnggi (iwfomdaaw d qdtky gr 2). Soaoidqw jtoih ndby d mgsldi hiqytkin (d tjslyq) unomn inyw jhy ig diidmz dtx xyrytx dkdothi ytysw jtoih. Rgq yvdsfay, iny hugqxhsdt ndh d mgsldi hiqytkin gr 11. Qdtkyx dtx tdbda jtoih ndby d hyfdqdiy mgsldi hiqytkin rgq qdtkyx diidmz dtx xyrythy.  Rgq yvdsfay, iny dqmnyq ndh d mgsldi hiqytkin gr 4 (jhyx rgq xyrytxotk) dtx d qdtkyx mgsldi hiqytkin gr 6 (jhyx rgq diidmzotk). Doq jtoih dqy ldhyx ot moioyh, mdt diidmz ytysw jtoih ot inyoq qdtky dtx inyw diidmz dtx xyrytx uoin inyoq mgsldi hiqytkin. Rgq yvdsfay, iny lgslyq ndh d qdtky gr 10 dtx d mgsldi hiqytkin gr 50.  Soaoidqw jtoih (yvmyfi doq jtoih) ndby d sgbysyti tjslyq gr ngu sdtw nyvyh inyw mdt sgby ot 1 ijqt. Tdbda jtoih mdt gtaw sgby ot udiyq nyvyh. Adtx jtoih dqy haguyx xgut ot qgjkn iyqqdot (noaah, rgqyhih, pjtkay), ot mqghhotk qobyqh dtx mdttgi fdhh inqgjkn sgjtidoth.

secret_key_guess = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".translate(str.maketrans(alphabet,key))
print(f"secret key:{secret_key}\nguess:     {secret_key_guess}")

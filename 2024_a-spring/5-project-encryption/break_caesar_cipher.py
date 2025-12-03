import random
from caesar_cipher import * 
#from nltk.corpus import words


text = "In Civilization V the frigate is a powerful ranged naval unit in the Renaissance era. The frigate can reach further destinations fast because it can enter deep ocean tiles and it has a movement of 5 hexes per turn. In addition, the frigate has a ranged combat strength of 28 (and  25 for defense), therefore it is very effective against land and naval units. Furthermore, frigates are very useful in conquering cities because of their combat strength and that multiple frigates can surround the city and can fire at it at the same time. On the other hand, the production cost is higher than any other unit in the Renaissance era and it consumes 1 iron, which is a strategic resource that is sometimes scarce. In summary, the frigate is a powerful ranged naval unit that is a game-changer in  Renaissance warfare."
secret_key = random.randint(1,25)
encrypted_text = encrypt_caesar(text, secret_key)


# for key in range(1,26):
#     print(f"key={key}  plain text beginning={decrypt_caesar(encrypted_text, key)[0:60]}")

# word_list = words.words()
# print(len(word_list))
# print(word_list[100:120])

with open('/Users/lorand/tmp/google-10000-english-usa.txt') as f:
    word_list = f.read().split()
# print(len(word_list))
# print(word_list[100:120])

numb_Engl_words_decrypt = {}
for key in range(1,26):
    count = 0
    plain_text = decrypt_caesar(encrypted_text, key)
    plain_text_words = plain_text.split()
    for v in plain_text_words:
        if v.lower() in word_list and len(v)>=3:
            count +=1
    numb_Engl_words_decrypt[key] = count
    #print(f"Key = {key} and number of English words = {count}")

#print(numb_Engl_words_decrypt)
print(f"Key with most English words after decryption = {max(numb_Engl_words_decrypt, key=numb_Engl_words_decrypt.get)}")

#input("And the secret key was... (press Enter to reveal)")
print(f"Secret key = {secret_key}")    
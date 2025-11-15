import random

def encrypt_caesar(plain_text, key):
    shift = key
    cipher_text = ""
    for v in plain_text:
        if v.isalpha() == True:
            if v.islower():
                ve = chr((ord(v) - ord("a") + shift) % 26 + ord("a"))
            else:
                ve = chr((ord(v) - ord("A") + shift) % 26 + ord("A"))
        else:
            ve = v
        cipher_text += ve
    return cipher_text


def decrypt_caesar(cipher_text, key):
    shift = key
    plain_text = ""
    for ve in cipher_text:
        if ve.isalpha() == True:
            if ve.islower():
                v = chr((ord(ve) - ord("a") - shift) % 26 + ord("a"))
            else:
                v = chr((ord(ve) - ord("A") - shift) % 26 + ord("A"))
        else:
            v = ve
        plain_text += v
    return plain_text    
    


text = "In Civilization V the frigate is a powerful ranged naval unit in the Renaissance era. The frigate can reach further destinations fast because it can enter deep ocean tiles and it has a movement of 5 hexes per turn. In addition, the frigate has a ranged combat strength of 28 (and  25 for defense), therefore it is very effective against land and naval units. Furthermore, frigates are very useful in conquering cities because of their combat strength and that multiple frigates can surround the city and can fire at it at the same time. On the other hand, the production cost is higher than any other unit in the Renaissance era and it consumes 1 iron, which is a strategic resource that is sometimes scarce. In summary, the frigate is a powerful ranged naval unit that is a game-changer in  Renaissance warfare."

encrypted_text = encrypt_caesar(text)
print(encrypted_text)

decrypted_text = decrypt_caesar(encrypted_text)
print(decrypted_text)


key = random.randint(1,25)
encrypted_text = encrypt_caesar(text, shift = key)

for shift in range(1,26):
    print(f"shift={shift}  plain text beginning={decrypt_caesar(encrypted_text, shift)[0:60]}")
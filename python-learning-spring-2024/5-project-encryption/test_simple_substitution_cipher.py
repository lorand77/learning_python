from simple_substitution_cipher import *

key = "DLMXYRKNOPZASTGFEQHIJBUVWC"
plain_text = "In Civilization V the tank is a powerful and highly mobile unit in the Atomic Era. The tank has the same combat strength as the infantry, and they are the most powerful units at the beginning of the Atomic Era. More importantly, the tank is a very mobile unit because it can move 5 hexes per turn and additionally it can move after attacking, thus it is very effective in hit-and-run tactics. However, the tank needs oil, thus you can build only a limited number of them, because you need the oil for other units, for example for bombers and battleships. In summary, the tank is a very effective unit on the battlefield, especially in hit-and-run tactics due to its high mobility."

cipher_text = encrypt_simple_substitution(plain_text, key)
print(cipher_text)

decrypted_text = decrypt_simple_substitution(cipher_text, key)
print(decrypted_text)
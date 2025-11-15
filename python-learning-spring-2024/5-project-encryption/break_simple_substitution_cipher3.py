from simple_substitution_cipher import *
import string
from utils import *

secret_key = "XYRKNJBUVWTGPMQHIDOCLFEZAS"
assert("".join(sorted(list(secret_key)))==string.ascii_uppercase)

plain_text = """
The offensive operation in southern France, originally scheduled to
be executed simultaneously with the Normandy landings, was conceived
with the aim of pushing northward from the southern coast, creating
a diversion of enemy troops from the northern assault, and generally
weakening the German Army in France. This operation was given the code
name ANVIL.
"""
# https://www.gutenberg.org/cache/epub/69911/pg69911.txt

plain_text = plain_text.translate(str.maketrans('', '', string.punctuation + string.digits + string.whitespace + "’")).lower()

cipher_text = encrypt_simple_substitution(plain_text, secret_key)
#print(cipher_text)

from collections import Counter
#print(Counter(cipher_text))

bigram = bigram(cipher_text)
print(Counter(bigram))

trigram = trigram(cipher_text)
print(Counter(trigram))


alphabet = ".........................."
key      = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += alphabet.lower()
key += key.lower()
reverse_substitution_table = str.maketrans(key, alphabet)
decrypted_text= cipher_text.translate(reverse_substitution_table)
print(decrypted_text)

#secret_key_guess = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".translate(str.maketrans(alphabet,key))
#print(f"secret key:{secret_key}\nguess:     {secret_key_guess}")



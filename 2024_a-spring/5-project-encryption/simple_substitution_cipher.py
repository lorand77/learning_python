def encrypt_simple_substitution(plain_text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += alphabet.lower()
    key += key.lower()
    substitution_table = str.maketrans(alphabet, key)
    cipher_text = plain_text.translate(substitution_table)
    return cipher_text


def decrypt_simple_substitution(cipher_text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += alphabet.lower()
    key += key.lower()
    reverse_substitution_table = str.maketrans(key, alphabet)
    plain_text = cipher_text.translate(reverse_substitution_table)
    return plain_text
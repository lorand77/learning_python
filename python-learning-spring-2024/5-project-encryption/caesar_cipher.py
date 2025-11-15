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

def bigram(text):
    bi = []
    for i in range(0,len(text)-1):
        bi.append(text[i:i+2])
    return bi


def trigram(text):
    tri = []
    for i in range(0,len(text)-2):
        tri.append(text[i:i+3])
    return tri
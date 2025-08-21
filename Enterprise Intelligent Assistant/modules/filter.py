BAD_WORDS = {"stupid", "idiot", "nonsense"}

def contains_bad_word(text):
    words = text.lower().split()
    return any(bad in words for bad in BAD_WORDS)

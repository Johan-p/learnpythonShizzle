def reverse(text):
    word = ""
    letter = len(text) - 1
    while letter >= 0:
        word = word + text[letter]
        letter = letter - 1
    return word
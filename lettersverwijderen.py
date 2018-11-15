def anti_vowel(text):
    output = ""
    for x in text:
        for i in "ieaouIEAOU":
            if x == i:
                x = ""
            else:
                x = x
        output = output + x
    return output
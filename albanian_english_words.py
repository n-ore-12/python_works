#def albanian_letter_freq():
    #alphabet_shqip = {"a": 0, "b": 0, "c": 0, "ç": 0, "d": 0, "dh": 0, "e": 0, "ë": 0, "f": 0, "g": 0, "gj": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "ll": 0, "m": 0, "n": 0, "nj": 0, "o": 0, "p": 0, "q": 0, "r": 0, "rr": 0, "s": 0, "sh": 0, "t": 0, "th": 0, "u": 0, "v": 0, "x": 0, "xh": 0, "y": 0, "z": 0, "zh": 0}


def english_letter_freq():
    alphabet_eng = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    with open("/Users/eduan/work/english.txt", "r") as file:
        text = file.read().lower()
    for i in text:
        if i in alphabet_eng:
            alphabet_eng[i] += 1

    most_common_letter = max(alphabet_eng, key=(alphabet_eng.get))
    least_common_letter = min(alphabet_eng, key=(alphabet_eng.get))
    print(f"The most common letter is {most_common_letter}, showing up {alphabet_eng[most_common_letter]} times.")
    print(f"The least common letter is {least_common_letter}, showing up {alphabet_eng[least_common_letter]} times.")

english_letter_freq()


def is_pangram(text):
    # text = text.strip().lower()
    # letters = []
    # for letter in text:
    #     if letter.isalpha():
    #         if letter not in letters:
    #             letters.append(letter)
    # if len(letters) != 26:
    #     return False
    # else:
    #     return True

    ##### refactor #####
    return len(dict((el, 0) for el in text.lower() if el.isalpha()).keys()) >= 26

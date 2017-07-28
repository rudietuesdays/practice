def is_isogram(text):
    text = text.strip().lower()
    dictionary = dict.fromkeys(text, 0)
    for letter in text:
        if letter.isalpha():
            dictionary[letter] += 1
    iso = True
    for letter in dictionary:
        if dictionary.get(letter) > 1:
            iso = False
    if iso == False:
        return False
    else:
        return True

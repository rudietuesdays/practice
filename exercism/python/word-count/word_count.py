import re

def word_count(string):
    string = string.lower()
    string = re.sub(r'[^a-zA-Z0-9]+|$', ' ', string)
    string = string.rstrip().split(' ')
    dictionary = {}
    for i in string:
        if i not in dictionary:
            dictionary[i] = 1
            print i
        else:
            dictionary[i] += 1
    return dictionary

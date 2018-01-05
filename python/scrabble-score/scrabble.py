import re

score_helper={
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

def score(word):
    return sum(
        [key for key, value in score_helper.items() if char.upper()
                            in value][0] for char
                            in word if not re.search(r'((\s+|\d+)|^$)', word)
    )

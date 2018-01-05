def is_isogram(word):
    chars = list(word.lower().replace(" ", "").replace("-", ""))
    for char in chars:
        test_list = chars
        if char in test_list:
            test_list.remove(char)
        if char in test_list:
            return False
    return True

def abbreviate(phrase):
    output = ""
    phrase = " ".join(phrase.split("-"))
    words = phrase.split(" ")
    for word in words:
        for char in word:

        output += word[0]
    return output.upper()

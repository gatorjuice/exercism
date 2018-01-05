


def say(number):
    zeros = len(str(number)) - 1
    output = ""
    return number / int("1{}".format("0"*(zeros)))

from string import ascii_uppercase
from string import digits

import random


class Robot(object):

    prev_names = []

    def __init__(self):
        self.pick_name()

    def reset(self):
        self.prev_names.append(self.name)
        while self.name in self.prev_names:
            self.pick_name()

    def pick_name(self):
        self.name = "{}{}".format(
            "".join(random.sample(ascii_uppercase, 2)),
            "".join(random.sample(digits, 3))
        )

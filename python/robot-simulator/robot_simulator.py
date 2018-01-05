NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.bearing = DIRECTIONS[(DIRECTIONS.index(self.bearing) + 1) % 4]

    def turn_left(self):
        self.bearing = DIRECTI3ONS[(DIRECTIONS.index(self.bearing) - 1) % 4]

    def advance(self):
        self.coordinates = tuple(map(sum,zip(self.coordinates,self.bearing)))

    def simulate(self, instructions):
        for char in instructions:
            if char == "A":
                self.advance()
            if char == "L":
                self.turn_left()
            if char == "R":
                self.turn_right()

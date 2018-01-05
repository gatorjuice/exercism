class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, slots):
        self.slots = [None for _ in xrange(slots)]
        print(self.slots)

    def read(self):
        value = None
        try:
            for slot in self.slots:
                if slot != None:
                    value = slot
                    self.slots.pop(0)
                    self.slots.append(None)
                    return value
        except Exception:
            raise BufferEmptyException

    def write(self, value):
        pass

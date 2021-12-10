class Rectangle:
    length = 0
    width = 0
    height = 0

    def __init__(self, a, b, c):
        self.length = int(a)
        self.width = int(b)
        self.height = int(c)
        if a < 0 or b < 0 or c < 0:
            raise ValueError()

    def calculate_volume(self):
        return self.length * self.width * self.height

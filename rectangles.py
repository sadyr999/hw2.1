class Rectangle:
    length = 0
    width = 0
    height = 0

    def __init__(self, a, b, c):
        try:
            temp_a = int(a)
            temp_b = int(b)
            temp_c = int(c)
        except:
            raise ValueError()

        if temp_a < 0 or temp_b < 0 or temp_c < 0:
            raise ValueError()

        self.length = int(a)
        self.width = int(b)
        self.height = int(c)

    def calculate_volume(self):
        return self.length * self.width * self.height

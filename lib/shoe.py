class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            print("Brand must be a string")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

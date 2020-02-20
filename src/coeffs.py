import random

COEFF_BOOKS = "COEFF_BOOKS"
COEFF_BOOKS_PER_DAY = "COEFF_BOOKS_PER_DAY"
COEFF_SUBSCRIPTION = "COEFF_SUBSCRIPTION"


class Coeff():
    def __init__(self):
        self.values = {}

    def __getitem__(self, item):
        if item not in self.values:
            return random.random()
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value
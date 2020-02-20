import random

COEFF_BOOKS = "COEFF_BOOKS"
COEFF_BOOKS_PER_DAY = "COEFF_BOOKS_PER_DAY"
COEFF_SUBSCRIPTION = "COEFF_SUBSCRIPTION"
COEFF_UNIQUE_BOOK = "COEFF_UNIQUE_BOOK"


class Coeff():
    def __init__(self):
        self.values = {
            COEFF_BOOKS: 3 * random.random(),
            COEFF_BOOKS_PER_DAY: 3 * random.random(),
            COEFF_SUBSCRIPTION: 3 * random.random(),
            COEFF_UNIQUE_BOOK: 3 * random.random()
        }

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value
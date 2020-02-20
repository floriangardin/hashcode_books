from src import parser, main
from src.coeffs import Coeff, COEFF_BOOKS
import random

from src.scorer import Scorer


class GenElement:

    def __init__(self):
        self.coeff = Coeff()
        self.score = 0

    def __init__(self, coeff1, coeff2):
        self.coeff = Coeff()
        i = 0
        for c in self.coeff.values.keys():
            self.coeff[c] = coeff1[c] if i % 2 == 0 else coeff2[c]
            i+=1


def get_score(books, libraries, B, L, D, coeff, scorer):
    result = main.compute_result(books, libraries, B, L, D, coeff)
    return scorer.score(result)


def compute_scores(books, libraries, B, L, D, pop, scorer):
    for element in pop:
        element.score = get_score(dict(books), dict(libraries), B, L, D, element.coeff, scorer)


def mix(element1, element2):
    return GenElement(element1.coeff, element2.coeff)


if __name__ == "__main__":

    filename = "b_read_on.txt"
    books, libraries, B, L, D = parser.parse(filename)
    scorer = Scorer(books, libraries, B, L, D)

    nb_gen = 4
    pop = [GenElement(Coeff(), Coeff()) for _ in range(nb_gen)]

    nb_iter = 10

    for i in range(nb_iter):
        compute_scores(books, libraries, B, L, D, pop, scorer)
        pop.sort(key=lambda element: element.score, reverse=True)
        for e in pop:
            print(e.score)
        print(pop[0].score)
        pop = pop[:int(len(pop)/2)]
        for i in range(len(pop)):
            pop.append(mix(pop[i], pop[int(len(pop)/2 - i - 1)]))


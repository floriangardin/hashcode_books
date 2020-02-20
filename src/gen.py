from src import parser
from src.coeffs import Coeff
import random


class GenElement:

    def __init__(self):
        self.coeff = Coeff()
        self.score = 0

    def __init__(self, coeff1, coeff2):
        self.coeff = Coeff()
        i = 0
        for c in self.coeff.values.keys():
            self.coeff = coeff1[c] if i % 2 == 0 else coeff2[c]
            i+=1


def get_score(coeff):
    return random.random()


def compute_scores(pop):
    for element in pop:
        element.score = get_score(element.coeff)


def mix(element1, element2):
    return GenElement(element1.coeff, element2.coeff)


if __name__ == "__main__":
    nb_gen = 64
    pop = [GenElement(Coeff(), Coeff()) for _ in range(nb_gen)]

    nb_iter = 10

    for i in range(nb_iter):
        compute_scores(pop)
        pop.sort(key=lambda element: element.score, reverse=True)
        for element in pop:
            print(element.score)
        pop = pop[:int(len(pop)/2)]
        for i in range(len(pop)):
            pop.append(mix(pop[i], pop[int(len(pop)/2 - i - 1)]))


from src import parser, main, submit
from src.coeffs import Coeff, COEFF_BOOKS
import random

from src.scorer import Scorer

import random
#random.seed(22)
#print(random.random())


class GenElement:

    def __init__(self, coeff1, coeff2):
        self.coeff = Coeff()
        i = 0
        for c in self.coeff.values.keys():
            self.coeff[c] = coeff1[c] if random.random() > 0.5 else coeff2[c]
            if random.random() > 0.9:
                self.coeff[c] = 3 * random.random()
            i+=1


def get_score(books, libraries, B, L, D, coeff, scorer):
    result = main.compute_result(books, libraries, B, L, D, coeff)
    return scorer.score(result)


def compute_scores(books, libraries, B, L, D, pop, scorer):
    for element in pop:
        element.score = get_score(dict(books), dict(libraries), B, L, D, element.coeff, scorer)


def mix(element1, element2):
    return GenElement(element1.coeff, element2.coeff)


list_file = [
    "d_tough_choices.txt",
    "e_so_many_books.txt",
    "f_libraries_of_the_world.txt"
]

if __name__ == "__main__":

    for filename in list_file:

        filename = "f_libraries_of_the_world.txt"
        books, libraries, B, L, D = parser.parse(filename)
        scorer = Scorer(books, libraries, B, L, D)

        nb_gen = 20
        pop = [GenElement(Coeff(), Coeff()) for _ in range(nb_gen)]

        nb_iter = 3

        for i in range(nb_iter):
            print("iteration: "+ str(i))
            compute_scores(books, libraries, B, L, D, pop, scorer)
            pop.sort(key=lambda element: element.score, reverse=True)
            for e in pop:
                print(e.score)
            print(pop[0].score)
            pop = pop[:int(len(pop)/2)]
            for i in range(len(pop)):
                pop.append(mix(pop[i], pop[int(len(pop)/2 - i - 1)]))

        result = main.compute_result(books, libraries, B, L, D, pop[0].coeff)
    
        submission = submit.Submission(result)

        submission.submit('sub/gen/sub_' + filename)


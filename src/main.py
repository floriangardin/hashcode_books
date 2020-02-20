import random

from src import parser, submit
from src.coeffs import Coeff, COEFF_BOOKS, COEFF_BOOKS_PER_DAY, COEFF_SUBSCRIPTION, COEFF_UNIQUE_BOOK

list_file = [
    "a_example.txt",
    "b_read_on.txt",
    "c_incunabula.txt",
    "d_tough_choices.txt",
    "e_so_many_books.txt",
    "f_libraries_of_the_world.txt"
]


def compute_result(books, libraries, B, L, D, coeff):
    result = []
    array_lib = list(libraries.values())
    book_nb_occu = {b.id : 0 for b in books.values()}
    for l in libraries.values():
        for b in l.books:
            book_nb_occu[b] += 1
    max_score_book = 0
    max_temps_sub = 0
    max_unique_book = 0
    max_book_per_day = 0
    min_score_book = 0
    min_temps_sub = 0
    min_unique_book = 0
    min_book_per_day = 0
    for l in array_lib:
        l.score_books = sum(books[b].score/(book_nb_occu[b] if book_nb_occu[b] > 0 else 1) for b in l.books)
        max_score_book = max(max_score_book, l.score_books)
        max_temps_sub = max(max_temps_sub, l.T)
        l.unique_book = sum([1 for b in l.books if book_nb_occu[b] == 1])
        max_unique_book = max(max_unique_book, l.unique_book)
        min_score_book = min(max_score_book, l.score_books)
        min_temps_sub = min(max_temps_sub, l.T)
        min_unique_book = min(max_unique_book, l.unique_book)

    den_score_book = max_score_book - min_score_book if max_score_book > min_score_book else 1
    den_temps_sub = max_temps_sub - min_temps_sub if max_temps_sub > min_temps_sub else 1
    den_unique_book = max_unique_book - min_unique_book if max_unique_book > min_unique_book else 1
    den_book_per_day = max_book_per_day - min_book_per_day if max_book_per_day > min_book_per_day else 1
    for l in array_lib:
        # score inv prop temps d'inscription
        # score
        l.score = coeff[COEFF_BOOKS] * (l.score_books - min_score_book) / (den_score_book) + \
             coeff[COEFF_BOOKS_PER_DAY] * (l.M - min_book_per_day) / (den_book_per_day) - \
             coeff[COEFF_SUBSCRIPTION] * (l.T - min_temps_sub) / (den_temps_sub) + \
             coeff[COEFF_UNIQUE_BOOK] * (l.unique_book - min_unique_book) / (den_unique_book)
    array_lib.sort(key=lambda l: l.score, reverse=True)
    for l in array_lib:
        result.append({
            "id_library": l.id,
            "books": [books[b] for b in l.books]
        })
        result[-1]["books"].sort(key=lambda b: b.score, reverse=True)
        result[-1]["books"] = [b.id for b in result[-1]["books"]]
    return result


def compute_result_brute_force(books, libraries, B, L, D):
    result = []
    array_lib = list(libraries.values())
    array_lib.sort(key=lambda l: l.score, reverse=True)

    day = 0
    scanned_books = set()
    while day < D:
        print(str(day) + "/" + str(D))
        best_id = -1
        max_score = 0
        for l in array_lib:
            l.books = l.books - scanned_books
            l.compute_score(books)
            if l.score > max_score:
                max_score = l.score
                best_id = l.id
        if best_id == -1:
            break
        result.append({
            "id_library": best_id,
            "books": [books[b] for b in libraries[best_id].books]
        })
        result[-1]["books"].sort(key=lambda b: b.score, reverse=True)
        result[-1]["books"] = [b.id for b in result[-1]["books"]]
        scanned_books = scanned_books | libraries[best_id].books
        day += libraries[best_id].T
        array_lib.remove(libraries[best_id])

    return result


if __name__ == "__main__":

    for file in list_file:
        print(file)
        books, libraries, B, L, D = parser.parse(file)
        for l in libraries.values():
            l.compute_score(books)

        result = compute_result(books, libraries, B, L, D)

        submission = submit.Submission(result)

        submission.submit('sub/sub_' + file)

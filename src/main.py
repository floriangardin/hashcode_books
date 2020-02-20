import random

from src import parser, submit
from src.coeffs import Coeff, COEFF_BOOKS, COEFF_BOOKS_PER_DAY, COEFF_SUBSCRIPTION

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
    array_lib.sort(key=lambda l: l.score, reverse=True)
    book_nb_occu = {b.id : 0 for b in books.values()}
    for l in libraries.values():
        for b in l.books:
            book_nb_occu[b] += 1
    for l in array_lib:
        l.score = coeff[COEFF_BOOKS] * sum(books[b].score/(book_nb_occu[b] if book_nb_occu[b] > 0 else 1) for b in l.books) * \
             l.M * \
             (D - coeff[COEFF_SUBSCRIPTION] * l.T)
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

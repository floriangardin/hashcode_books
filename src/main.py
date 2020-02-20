from src import parser, submit

list_file = [
    "a_example.txt",
    "b_read_on.txt",
    "c_incunabula.txt",
    "d_tough_choices.txt",
    "e_so_many_books.txt",
    "f_libraries_of_the_world.txt"
]

if __name__ == "__main__":

    for file in list_file:
        books, libraries, B, L, D = parser.parse(file)

        result = []

        for l in libraries.values():
            l.compute_score(books)

        array_lib = list(libraries.values())
        array_lib.sort(key=lambda l: l.score, reverse=True)

        for l in array_lib:
            result.append({
                "id_library": l.id,
                "books": [books[b] for b in l.books]
            })
            result[-1]["books"].sort(key=lambda b: b.score, reverse=True)
            result[-1]["books"] = [b.id for b in result[-1]["books"]]

        submission = submit.Submission(result)

        submission.submit('data/sub_' + file)

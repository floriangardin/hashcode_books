from src import parser
from src import submit
from src.parser import parse
from src.scorer import Scorer
from src.submit import Submission


list_file = [
    #"b_read_on.txt",
    #"a_example.txt",
    "d_tough_choices.txt"
]

if __name__ == '__main__':

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

        scorer = Scorer(books, libraries, B, L, D)

        score = scorer.score(result)

        print('Score is ', score)

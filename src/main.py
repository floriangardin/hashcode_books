from src import parser, submit

if __name__ == "__main__":
    books, libraries = parser.parse("a_example.txt")

    result = []

    for l in libraries.values():
        l.compute_score(books)
        print(l.score)

    array_lib = list(libraries.values())
    array_lib.sort(key=lambda l: l.score, reverse=True)

    for l in array_lib:
        result.append({
            "id_library": l.id,
            "books": [books[b] for b in l.books]
        })
        result[-1]["books"].sort(key=lambda b: b.score, reverse=True)
        result[-1]["books"] = [b.id for b in result[-1]["books"]]

    print(result)

    submission = submit.Submission(result)

    submission.submit('data/submission.txt')

from src.parser import parse
from src.scorer import Scorer


class Submission:
    def __init__(self, libraries):
        """
        librairies : [{'id_library': int, books: [int]}]
        :param nb_librairies:
        :param librairies:
        """
        self.libraries = libraries


    def submit(self, filename):
        with open(filename, 'w') as f:
            scanned_books = set()
            for library in self.libraries:
                library['books'] = [b for b in library["books"] if b not in scanned_books]
                scanned_books |= set(library['books'])

            f.write(str(len([l for l in self.libraries if len(l["books"]) > 0])))
            for library in self.libraries:
                if len(library['books']) == 0:
                    continue
                f.write('\n')
                f.write(str(library['id_library']) + " " + str(len(library['books'])))
                f.write('\n')
                f.write(" ".join([str(book) for book in library['books']]))








## Test Easy solution
if __name__ == '__main__':

    books, libraries, B, L, D = parse("a_example.txt")

    for l in libraries:
        print(libraries[l])

    scorer = Scorer(books)


    submission = Submission([{'id_library': 1, 'books': [1, 2, 3 ]},
                             {'id_library': 2, 'books': [5, 6, 7]}])

    submission.submit('data/submission.txt')

from src.parser import parse



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
            f.write(str(len(self.libraries)))
            f.write('\n')

            for library in self.libraries:
                if len(library['books']) == 0:
                    continue
                f.write(str(library['id_library']) + " " + str(len(library['books'])))
                f.write('\n')
                f.write(" ".join([str(book) for book in library['books']]))
                f.write('\n')



class Scorer:

    def __init__(self, books):
        self.books = books
        self.score_dict = {key: val.score for key, val in books.items()}

    def score(self, submission, D):

        for library in self.libraries:

            from pdb import set_trace; set_trace()

            if False:
                break

        pass



## Test Easy solution
if __name__ == '__main__':

    books, libraries, B, L, D = parse("a_example.txt")

    for l in libraries:
        print(libraries[l])

    scorer = Scorer(books)


    submission = Submission([{'id_library': 1, 'books': [1, 2, 3 ]},
                             {'id_library': 2, 'books': [5, 6, 7]}])

    submission.submit('data/submission.txt')

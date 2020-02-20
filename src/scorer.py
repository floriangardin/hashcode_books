from pdb import set_trace

class Scorer:

    def __init__(self, books, libraries, B, L, D):
        self.books = books
        self.libraries = libraries
        self.score_dict = {key: val.score for key, val in books.items()}
        self.B = B
        self.L = L
        self.D = D

    def score(self, submission):

        days = 0
        days_remaining = {}  # id_library: nb_days

        # Find days remaining
        for library_dict in submission:
            id = library_dict['id_library']
            books = library_dict['books']
            days += self.libraries[id].T
            if days >= self.D:
                break
            days_remaining[id] = {'days_remaining': self.D - days, 'books': books}

        # Score
        points = 0

        books_completed = set()

        for library_id, remain in days_remaining.items():
            days = remain['days_remaining']
            books = remain['books']
            d = 0
            to_break = False
            #print('Nb books', len(books), "Days", days, "Days register", self.libraries[library_id].T,  "Number books per day", self.libraries[library_id].M)
            for book in books:
                points_multiplier = 1

                if book in books_completed:
                    points_multiplier = 0

                books_completed.add(book)
                d += 1/self.libraries[library_id].M
                points += points_multiplier * self.score_dict[book]
                if d >= days:
                    break



        return points
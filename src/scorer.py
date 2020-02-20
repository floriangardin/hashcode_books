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
            days_remaining[id] = {'days_remaining': self.D - days, 'books': books}

            if days >= self.D:
                break

        # Score
        points = 0
        for library_id, remain in days_remaining.items():

            days = remain['days_remaining']
            books = remain['books']
            d = 0
            for book in books:

                points += self.score_dict[book]
                d += 1/self.libraries[library_id].N
                if d > days:
                    break
        return points
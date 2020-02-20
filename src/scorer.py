class Scorer:

    def __init__(self, books, libraries, B, L, D):
        self.books = books
        self.libraries = libraries
        self.score_dict = {key: val.score for key, val in books.items()}
        self.B = B
        self.L = L
        self.D = D

    def score(self, submission):

        #from pdb import set_trace; set_trace()
        days = 0
        days_remaining = {}  # id_library: nb_days

        print('Days', self.D)

        # Find days remaining
        for library_dict in submission:

            id = library_dict['id_library']
            books = library_dict['books']
            days += self.libraries[id].T
            days_remaining[id] = {'days_remaining': self.D - days, 'books': books}

            if days >= self.D:
                print('I break')
                break

        # Score
        points = 0

        books_completed = set()

        for library_id, remain in days_remaining.items():
            days = remain['days_remaining']
            books = remain['books']
            d = 0
            to_break = False
            #print('Library', library_id, "days", d)
            for book in books:
                points_multiplier = 1
                if book in books_completed:
                    points_multiplier = 0

                books_completed.add(book)
                #print('Book', book, "days", d, "points", points)
                points += points_multiplier * self.score_dict[book]
                d += 1/self.libraries[library_id].N
                if d >= days:
                    to_break = True
                    print('I break 2 ')
                    break
            if to_break:
                break

        return points
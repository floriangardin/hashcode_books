import os


class library:
    def __init__(self, id, N, T, M):
        self.id = id
        self.N = N
        self.T = T
        self.M = M
        self.books = set()

    def add_books(self, s):
        self.books = s

    def __str__(self):
        return "library " + str(self.id) + " takes " + str(self.T) + " days to sign up, possesses " + str(self.N) + " books, and can scan " + str(self.M) + " books per day"


class book:
    def __init__(self, id):
        self.id = id


def parse(filename):
    tabs = []
    with open(os.getcwd() + "/data/" + filename) as fichier:
        for line in fichier:
            tabs += [line[:-1]]
    i = 0
    B = 0
    L = 0
    D = 0
    books = {}
    libraries = {}
    for line in tabs:
        if i == 0:
            B = int(line.split(" ")[0])
            L = int(line.split(" ")[1])
            D = int(line.split(" ")[2])
        if i == 1:
            id = 0
            for s in line.split(" "):
                books[id] = book(int(s))
                id += 1
        if i > 1:
            if i % 2 == 0:
                lib_index = (i-2) / 2
                libraries[lib_index] = library(lib_index, int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]))
            else:
                lib_index = (i - 3) / 2
                libraries[lib_index].add_books(set([int(a) for a in line.split(" ")]))
        i += 1
    return books, libraries


if __name__ == "__main__":
    books, libraries = parse("a_example.txt")
    for l in libraries:
        print(libraries[l])

    from pdb import set_trace; set_trace()
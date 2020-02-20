from src.parser import parse



class Submission:
    def __init__(self, librairies):
        """
        librairies : {'id_library': int, books: [int]}
        :param nb_librairies:
        :param librairies:
        """




    def submit(self, filename):


        with open(filename, 'w') as f:
            f.write()


books, libraries = parse("a_example.txt")
for l in libraries:
    print(libraries[l])


## Easy solution

from pdb import set_trace; set_trace()
submission = Submission(librairies)

submission.submit('data/submission.txt')

from pdb import set_trace; set_trace()
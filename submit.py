from src.parser import parse



books, libraries = parse("a_example.txt")
    for l in libraries:
        print(libraries[l])
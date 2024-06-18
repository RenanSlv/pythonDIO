import itertools

string = input("String a ser permutada: ")

restultado = itertools.permutations(string, len(string))

for i in restultado:
    print(''.join(i))


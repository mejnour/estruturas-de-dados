lista = []
reverse = False

def le(linha):
    global reverse
    quebra = []
    quebra = linha.split(' ')

    if reverse is False:

        if quebra[0] == 'back':
            if len(lista) == 0 or lista[len(lista) - 1] is None:
                print('No job for Ada?')
            else:
                print(lista[len(lista) - 1])
                lista.pop(lista[len(lista) - 1])

        elif quebra[0] == 'front':
            if len(lista) == 0 or lista[0] is None:
                print('No job for Ada?')
            else:
                print(lista[0])
                lista.pop(0)

        elif quebra[0] == 'reverse':
            reverse = True

        elif quebra[0] == 'push_back':
            lista.append(quebra[1])

        elif quebra[0] == 'toFront':
            lista.insert(0, quebra[1])

    else:

        if quebra[0] == 'back':
            if len(lista) == 0 or lista[0] is None:
                print('No job for Ada?')
            else:
                print(lista[0])
                lista.pop(lista[0])

        elif quebra[0] == 'front':
            if len(lista) == 0 or lista[len(lista) - 1] is None:
                print('No job for Ada?')
            else:
                print(lista[len(lista) - 1])
                lista.pop(lista[len(lista) - 1])

        elif quebra[0] == 'reverse':
            reverse = False

        elif quebra[0] == 'push_back':
            lista.insert(0, quebra[1])

        elif quebra[0] == 'toFront':
            lista.append(quebra[1])


def processa(ops):
    para = len(ops)
    index = 0
    while para > 0:
        try:
            le(ops[index])
        except:
            return 0
        index += 1
        para -= 1


if __name__ == "__main__":
    Q = int(input())
    ops = []
    while Q > 0:
        ops.append(input())
        Q -= 1

    processa(ops)

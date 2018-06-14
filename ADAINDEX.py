def procura(prefix, data):
    cont = 0
    auxL = 0
    auxK = 0

    while auxK < len(prefix):
        k = prefix[auxK]
        tam = len(k)
        cont = 0

        auxL = 0
        while auxL < len(data):
            l = data[auxL]

            if k == l[0:tam]:
                cont += 1

            auxL += 1

        print('{}'.format(cont))
        auxK += 1


if __name__ == '__main__':
    data = []
    pref = []

    inp = input().split()

    N = int(inp[0])
    Q = int(inp[1])

    while N > 0:
        data.append(input())
        N -= 1

    while Q > 0:
        pref.append(input())
        Q -= 1

    procura(pref, data)

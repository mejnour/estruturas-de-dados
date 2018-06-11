class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def setDado(self, novoDado):
        self.dado = novoDado

    def setProx(self, novoProx):
        self.prox = novoProx

    def getDado(self):
        return self.dado

    def getProx(self):
        return self.prox


class LSE:
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.tamanho

    def add(self, dado):
        temp = No(dado)
        temp.setProx(self.head)
        self.head = temp

        self.tamanho = self.tamanho + 1

    def search(self, item):
        atual = self.head
        achou = False
        while atual is not None and achou is False:
            if atual.getDado() == item:
                achou = True
            else:
                atual = atual.getProx()

        return achou

    def remove(self, item):
        atual = self.head
        anterior = None
        removed = False
        while atual is not None and removed is False:
            if atual.getDado() == item:
                removed = True
            else:
                anterior = atual
                atual = atual.getProx()

        if anterior is None:
            self.head = atual.getProx()
            self.tamanho -= 1
        elif removed is False:
            print(removed)
        else:
            anterior.setProx(atual.getProx())
            self.tamanho -= 1


if __name__ == "__main__":
    lista = LSE()
    lista.add(1)
    lista.add(2)
    lista.add(3)

    print(lista.size())
    # print(lista.search(1))
    lista.remove(3)
    print(lista.size())
    print(lista.search(3))

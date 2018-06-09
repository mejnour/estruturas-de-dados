class No:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, novoDado):
        self.novoDado = novoDado

    def setNext(self, novoNext):
        self.novoNext = novoNext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class UnorderList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        tam = self.size
        return tam

    def add(self, dado):
        temp = No(dado)
        temp.setNext(self.head)
        self.head = temp
        self.size = self.size + 1


if __name__ == "__main__":
    lista = UnorderList()
    lista.add(1)
    lista.add(2)
    print(lista.size())

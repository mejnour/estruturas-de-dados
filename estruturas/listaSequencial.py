#coding: utf-8


class ListaSeq:
    def __init__(self, tamMax):
        self.dados = []
        self.tamMax = tamMax
        self.tamAtual = 0

    def vazia(self):
        if self.tamAtual is None:
            return True
        else:
            return False

    def cheia(self):
        if self.tamAtual == self.tamMax:
            return True
        else:
            return False

    def tamanho(self):
        return self.tamAtual

    def elemento(self, item):
        achou = False
        for i in self.dados:
            # print(i)
            if i == item:
                achou = True

        if achou is False:
            print("Item não existe")
            return False
        else:
            return item

    def posicao(self, item):
        achou = False

        for i in self.dados:
            print(i)
            if i == item:
                achou = True

        if achou is False:
            print("Item não existe")
        else:
            return item

    def mostra(self):
        for i in self.dados:
            print(i)

    def insere(self, pos, item):
        if self.cheia() or pos > self.tamMax or pos < 1:
            print('Posição inválida')
            return False

        # print(pos)
        # print(len(self.dados))

        if (self.tamAtual == 0) or (pos - 1 == len(self.dados)):
            self.dados.append(item)
            self.tamAtual += 1

            # print("{} --".format(len(self.dados)))
            return item
        else:
            self.dados.append(self.dados[len(self.dados) - 1])
            # print(self.dados[len(self.dados) - 1])
            for i in range(len(self.dados) - 1, pos - 1, -1):
                # print('i: {}'.format(i))
                self.dados[i] = self.dados[i - 1]

            self.dados[pos - 1] = item
            self.tamAtual += 1

            # print("{} --".format(len(self.dados)))
            return item

    def remove(self, pos):
        pass


if __name__ == '__main__':
    lista = ListaSeq(10)
    lista.insere(1, 0)
    lista.insere(2, 1)
    lista.insere(3, 2)
    lista.insere(4, 3)
    lista.insere(5, 4)

    lista.insere(3, 5)
    lista.insere(3, 5)
    lista.insere(3, 5)
    lista.insere(3, 5)
    lista.insere(3, 5)
    lista.insere(3, 5)
    # lista.insere(2, 5)
    # print(lista.vazia())
    # print(lista.cheia())
    # print(lista.tamanho())
    lista.mostra()
    # print(lista.elemento(2))
    # print(lista.elemento(5))
    # print(lista.posicao(1))
    # print(lista.posicao(2))
    # print(lista.posicao(3))
    # print(lista.posicao(4))
    # print(lista.posicao(5))

#encoding: utf-8
# A definição de classe é assim mesmo
# class <Nome>:
class BinaryTree:
    # Praticamente toda função recebe ela própria (self)

    # Construtor da classe tem o __init__
    # os self.<algumacoisa> são os atributos da classe
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # Insere a esquerda
    # Testa primeiro se já tem alguma coisa
    # se não tem, ela empurra o que tiver pra baixo
    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # Insere a direita
    # Mesma coisa do insere a esquerda
    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.insertRight = t

    # Getters e Setters necessários
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# Função externa de caminhamento
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())


# Não existe 'main' em python. Tudo é 'main'
# pode-se entender os comandos abaixo como inseridos
# em um hipotetico 'main'
# Manipulações
r = BinaryTree('a')
# print(r.getRootVal())

# print(r.getLeftChild())
r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())

r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
#
r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

# postorder(r)
# preorder(r)
# inorder(r)

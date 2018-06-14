class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(inOrd, preOrd, inStr, inEnd):
    if (inStr > inEnd):
        return None

    tNode = Node(preOrd[buildTree.preIndex])
    buildTree.preIndex += 1

    if inStr is inEnd:
        return tNode

    inIndex = search(inOrd, inStr,  inEnd, tNode.data)

    tNode.left = buildTree(inOrd, preOrd, inStr, inIndex - 1)
    tNode.right = buildTree(inOrd, preOrd, inIndex + 1, inEnd)

    return tNode


def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i


def printInorder(node):
    if node is None:
        return

    printInorder(node.left)
    print(node.data, end = " ")
    printInorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    # print(node.data, end = " ")
    posVec.append(node.data)


def cospe():
    if ((posVec > posOrder) - (posVec < posOrder)) is 0:
        print('yes\n')
    else:
        print('no\n')

if __name__ == '__main__':
#     preOrder = ['1', '2', '4', '5', '3', '6']
#     posOrder = ['4', '5', '2', '6', '3', '1']
#     inOrder = ['4', '2', '5', '1', '3', '6']

    # preOrder = ['1', '2', '4', '5', '3', '6']
    # posOrder = ['4', '5', '2', '6', '1', '3']
    # inOrder = ['4', '2', '5', '1', '6', '3']

    posVec = []

    nos = int(input())
    preOrder = input().split(' ')
    posOrder = input().split(' ')
    inOrder = input().split(' ')

    # print(preOrder, posOrder, inOrder, sep = '\n')

    buildTree.preIndex = 0
    while 1:
        try:
            root = buildTree(inOrder, preOrder, 0, nos-1)
            postorder(root)
            cospe()
            break
        except:
            print('no\n')
            break

    # print(posVec is posOrder)
    # print(((posVec > posOrder) - (posVec < posOrder)))

    # print("Inorder traversal of the constructed tree is")
    # printInorder(root)
    # print('')
    #
    # postorder(root)
    # print('')

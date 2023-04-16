from Node import Node
from colorama import Fore, Back, Style

class RBtree:
    def __init__(self):
        self.root = None
        self.tree_size = 0

    def insert(self, value):
        node = Node(value)
        node.value = value
        node.color = 'R'
        self.tree_size = self.tree_size + 1

        x = self.root
        while x != None:  # Find position for new node
            node.parent = x  # and set the last none null node as it's parent
            if node.value < x.value:
                x = x.left
            else:
                x = x.right

        if node.parent == None:  # If parent is null, then it is root node
            self.root = node
            node.color = 'B'
            return
        elif node.value < node.parent.value:  # Check if it is right Node or Left Node by checking the value
            node.parent.left = node
        else:
            node.parent.right = node

        if node.parent.parent == None:  # If parent of node is Root Node
            return
        self.fix_insertion(node)  # fix last insertion

    def rotate_left(self, parent):
        node = parent.right
        parent.right = node.left
        if node.left != None:
            node.left.parent = parent

        node.parent = parent.parent  # Change parent of y as parent of x
        if parent.parent == None:  # If parent of x == None ie. root node
            self.root = node  # Set y as root
        elif parent == parent.parent.left:
            parent.parent.left = node
        else:
            parent.parent.right = node
        node.left = parent
        parent.parent = node

    def rotate_right(self, parent):
        node = parent.left
        parent.left = node.right
        if node.right != None:
            node.right.parent = parent

        node.parent = parent.parent
        if parent.parent == None:
            self.root = node
        elif parent == parent.parent.right:
            parent.parent.right = node
        else:
            parent.parent.left = node
        node.right = parent
        node.parent = parent

    def fix_insertion(self, node):
        while (node.parent != None):  # as long the parent isn't black or None
            if (node.parent.color == 'R'):  # enter the loop
                if (node.parent.parent.right == node.parent):  # if the parent is a right child
                    uncle = node.parent.parent.left
                    if (uncle != None and uncle.color == 'R'):  # and the uncle is red too
                        uncle.color = 'B'  # only change the colors
                        node.parent.color = 'B'
                        node.parent.parent.color = 'R'
                        node = node.parent.parent  # turn the grandparent node Red and start again
                    else:  # the uncle is Black
                        if (node == node.parent.left):  # if the node is a left child to a right child parent
                            node = node.parent
                            self.rotate_right(node)  # rotate right first then rotate left
                        node.parent.color = 'B'
                        node.parent.parent.color = 'R'
                        self.rotate_left(node.parent.parent)  # ###################################################
                else:  # the parent is a left child
                    uncle = node.parent.parent.right
                    if (uncle != None and uncle.color == 'R'):  # and the uncle is red too
                        uncle.color = 'B'  # only change the colors
                        node.parent.color = 'B'
                        node.parent.parent.color = 'R'
                        node = node.parent.parent  # turn the grandparent node Red and start again
                    else:  # the uncle is Black
                        if (node == node.parent.right):  # if the node is a right child to a Left child parent
                            node = node.parent
                            self.rotate_left(node)  # rotate left first then rotate right
                        node.parent.color = 'B'
                        node.parent.parent.color = 'R'
                        self.rotate_right(node.parent.parent)
            else:  # break if the node is black
                break
            self.root.color = 'B'

    def depth(self):

        def max_depth(node):
            if (node == None):
                return 0
            return max(max_depth(node.left), max_depth(node.right)) + 1

        return max_depth(self.root) - 1

    def size(self):
        return self.tree_size

    def search(self, value):

        def tree_search(node):
            if(node != None):
                if(node.value == value):
                    return node
                elif(node.value < value):
                    return tree_search(node.right)
                else:
                    return tree_search(node.left)
            else:
                return node

        return tree_search(self.root)

    def print_RBtree(self):
        arr = []
        max_spaces = int(pow(2, self.depth()))
        arr.append(self.root)

        def num_of_nums(arr):
            num = len(arr)
            for i in arr:
                if (i == ' '):
                    num -= 1
            return num

        while (num_of_nums(arr) != 0):
            length = len(arr)
            for j in range(0, length):
                for k in range(max_spaces):
                    print('  ', end='')
                if (arr[0] != ' '):
                    if (arr[0].left != None):
                        arr.append(arr[0].left)
                    else:
                        arr.append(' ')
                    if (arr[0].right != None):
                        arr.append(arr[0].right)
                    else:
                        arr.append(' ')
                    if(arr[0].color == 'R'):
                        print(Fore.RED + f"{arr.pop(0).value}", end='')
                        print(Style.RESET_ALL, end='')
                    else:
                        print(arr.pop(0).value, end='')
                else:
                    arr.append(' ')
                    arr.append(' ')
                    print(arr.pop(0), end='')
                for k in range(max_spaces):
                    print('  ', end='')
            max_spaces = max_spaces // 2
            print('\n')

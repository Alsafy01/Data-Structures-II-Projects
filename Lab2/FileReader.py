from RedBlackTree import RBtree


class Dictionary:
    def __init__(self):
        self.path = "EN-US-Dictionary.txt"
        self.dictionary = ''
        self.dictionaryData = ''
        self.dictionaryTree = ''

    def loadDictionary(self):
        self.dictionary = open(self.path, 'r')
        self.dictionaryData = self.dictionary.readlines()
        self.dictionary.close()
        self.dictionaryTree = RBtree()
        for i in range(0, len(self.dictionaryData)):
            if self.dictionaryData[i] != None:
                self.dictionaryTree.insert(self.dictionaryData[i].strip())

    def printDictionary(self):
        print("size:", self.dictionaryTree.size())
        print("depth:", self.dictionaryTree.depth())
        self.dictionaryTree.print_RBtree()

    def insertWord(self):
        print("Enter the word: ")
        word = input().strip()
        if (self.dictionaryTree.search(word) == None):
            self.dictionary = open(self.path, 'a')
            self.dictionary.write("\n" + word)
            self.dictionary.close()
            self.dictionaryTree.insert(word)
        else:
            print("ERROR: Word already in the dictionary!")

    def lookUp(self):
        print("Enter the word you want to search: ")
        lookUpWord = input()
        if (self.dictionaryTree.search(lookUpWord) == None):
            print("NO")
        else:
            print("YES")

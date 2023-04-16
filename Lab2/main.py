from RedBlackTree import RBtree
from FileReader import Dictionary

tree = RBtree()
for i in range(1, 11):
    tree.insert(i)

print("size:", tree.size())
print("depth:", tree.depth())
tree.print_RBtree()

dictionary=Dictionary()
dictionary.loadDictionary()
dictionary.printDictionary()
print("Inserting Word")
dictionary.insertWord()
dictionary.lookUp()
# dictionary=open("Dictionary.txt",'a')
# dictionaryData=dictionary.readlines()
# dictionary.close()
# dictionaryTree=RBtree()

# for i in range(0,len(dictionaryData)):
#     dictionaryTree.insert(dictionaryData[i])

# print("size:", dictionaryTree.size())
# print("depth:", dictionaryTree.depth())
# dictionaryTree.print_RBtree()
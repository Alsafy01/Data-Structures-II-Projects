from RedBlackTree import RBtree

tree = RBtree()
for i in range(1, 11):
    tree.insert(i)

print("size:", tree.size())
print("depth:", tree.depth())
tree.print_RBtree()



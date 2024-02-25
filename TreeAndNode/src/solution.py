from TreeAndNode.models.Node import Node
from TreeAndNode.models.Tree import Tree

root = Tree(Node(5))
v = root.get_root()

n1 = Node(3)
n2 = Node(4)
n3 = Node(1)
root.root.append_children([n1, n2])
n2.append_child(n3)

root.root.get_children()

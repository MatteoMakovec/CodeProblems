from .Node import Node


class Tree:
    def __init__(self, root: Node) -> None:
        self.root = root

    def get_root(self) -> Node:
        return self.root

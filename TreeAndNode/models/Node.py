from typing import List


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.children = []

    def append_child(self, child: 'Node') -> None:
        self.children.append(child)

    def append_children(self, children: List['Node']) -> None:
        for c in children:
            self.children.append(c)

    def get_value(self) -> int:
        return self.value

    def get_children(self) -> None:
        for c in self.children:
            print(c.value)

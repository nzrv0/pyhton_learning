class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_first(self, elem):
        elem.next = self.head
        self.head = elem

    def add_last(self, elem):
        current = self.head

        if current:
            while current.next:
                current = current.next
            current.next = elem
        else:
            self.head = elem

    def __repr__(self) -> str:
        node = self.head

        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


first_node = Node("A")
second_node = Node("B")
third_node = Node("C")

llist = LinkedList()
llist.head = first_node
llist.add_first(second_node)
llist.add_last(third_node)

print(llist)
